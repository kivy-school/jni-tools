# Wrapping an external Java module as a reusable pyjnius package

When you wrap an Android SDK (`.aar`) you almost always reference Java
types that live *outside* of that SDK — `android.content.Intent`,
`android.os.Bundle`, `android.app.Activity`, `java.lang.Runnable`, and so
on. Out of the box `jni-wrap` handles each unresolved reference in
the generated `.pyi` files by synthesizing a forward-declared empty stub
class at the top of every file that needs it. That keeps the IDE happy
but produces a lot of duplicated stubs across the tree.

The recipe below shows how to wrap a shared library (here, the Android
framework `android.jar`) once into its own pyjnius package, then point
every downstream wrapper at it via the `--external-module` flag so they
emit real `from android.content.Intent import Intent` lines instead of
re-stubbing.

The same recipe applies to any external dependency: `gms.jar`,
`firebase-*.jar`, `kotlin-stdlib.jar`, etc.

---

## 1. The `.pyi` resolution pipeline

For every Java type referenced by a wrapper, the `.pyi` emitter walks
this priority list:

| # | Tier                          | Result                                                 |
|---|-------------------------------|--------------------------------------------------------|
| 1 | Built-in mapping              | `String → str`, `List → list`, primitives, …           |
| 2 | Same-file nested              | quoted forward ref: `"Companion"`, `"UseThread"`       |
| 3 | Cross-file wrapped            | real import + bare name (`from x.y.Z import Z`)        |
| 4 | **External package mapping**  | real import from a pre-wrapped package — *this doc*    |
| 5 | Unwrapped external (fallback) | synthesize empty stub class at top of file             |
| 6 | Last resort                   | `Any` (e.g. `java.lang.Object`)                        |

Tier 5 (synthesized stubs) carries a docstring with the full Java FQCN
and a best-effort JavaDoc URL routed by namespace:

| Namespace prefix                                  | URL host                                    |
|---------------------------------------------------|---------------------------------------------|
| `android.` / `androidx.` / `dalvik.`              | developer.android.com/reference             |
| `java.` / `javax.` / `org.w3c.` / `org.xml.`      | docs.oracle.com/javase/8/docs/api           |
| `kotlin.` / `kotlinx.`                            | kotlinlang.org/api/latest/jvm/stdlib        |
| `com.google.android.gms.` / `com.google.firebase.`| developers.google.com/android/reference     |
| anything else                                     | docstring without URL                       |

Arrays whose element type would resolve to `Any` collapse to bare `list`
instead of `list[Any]` (pyjnius maps Java arrays to Python lists at
runtime, so the typed form would be misleading).

---

## 2. The `--external-module` flag

```text
--external-module <java.prefix.>=<python.prefix>     (repeatable)
```

Promotes tier 4 over tier 5 for any Java FQCN starting with
`<java.prefix.>`. The Java prefix **must end with `.`** so that
`android.` cannot accidentally match `androidx.`; the CLI rejects
prefixes without a trailing dot.

Examples:

```sh
# Long form
--external-module android.=android

# Short form (defaults py-prefix to the java prefix minus the trailing dot)
--external-module android.

# Multiple
--external-module android. --external-module javax.inject.=javax.inject
```

For a Java FQCN `android.content.Intent` and mapping
`android.=android`, the emitter writes:

```python
from android.content.Intent import Intent
```

This matches the per-class file layout produced by `jni-wrap` when
run with `--keep-package-prefix`, which is how the upstream wrapper
package needs to be generated (see next section).

---

## 3. Recipe: wrap `android.jar`, then point examples at it

### 3.1. Generate the upstream package once

```sh
cd pyjnius-builder/jni-wrapper

swift run --package-path JniWrap jni-wrap \
    --keep-package-prefix \
    ~/.psproject/android-sdk/platforms/android-35/android.jar \
    examples/android/src
```

`--keep-package-prefix` is required so the package root ends up literally
at `examples/android/src/android/…` instead of being stripped down to
some shorter common prefix. The resulting `pyproject.toml` ships only
`packages = ["src/android"]`, so dalvik/java/javax/org roots that
`android.jar` also contains are dropped at wheel build time.

Output: ~4267 `.py` + 3976 `.pyi` files. Size cost is a one-time hit;
treat this generated package like vendored content.

### 3.2. Regenerate downstream wrappers with the flag

```sh
swift run --package-path JniWrap jni-wrap \
    --external-module android.=android \
    /tmp/wrap-demo/onesignal4.aar \
    examples/onesignal/src/onesignal_pyjnius

swift run --package-path JniWrap jni-wrap \
    --external-module android.=android \
    /tmp/wrap-demo/admob-api.aar \
    examples/admob/src/admob_pyjnius
```

### 3.3. Declare the dependency

In each downstream `pyproject.toml`:

```toml
[project]
dependencies = ["pyjnius", "android-pyjnius"]
```

---

## 4. What downstream `.pyi`s look like after wiring

Before (synthesized stub at top of every file):

```python
from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Intent:
    """Forward declaration for ``android.content.Intent``. …"""
    ...

class ADMMessageHandler:
    def onMessage(self, arg0: Intent) -> None: ...
```

After (real import resolves via `android-pyjnius`):

```python
from typing import Any, ClassVar, overload
from android.content.Intent import Intent

class ADMMessageHandler:
    def onMessage(self, arg0: Intent) -> None: ...
```

Verification grep that should return zero matches after regeneration:

```sh
grep -rE 'class (Intent|Context|Bundle|Activity): \.\.\.' \
    examples/onesignal/src examples/admob/src
```

---

## 5. Future direction

The generated `examples/android/` package is a **temporary** stand-in.
The plan is to replace it with a hand-curated `android-pyjnius`
published to PyPI; downstream wrappers depend on it *by name* already,
so the swap is transparent.

The same approach should be applied to:

- `com.google.android.gms.` → a `gms-pyjnius` upstream package.
- `com.google.firebase.`    → a `firebase-pyjnius` upstream package.
- `kotlin.` / `kotlinx.`    → a `kotlin-stdlib-pyjnius` upstream package.

Until those exist, references to those namespaces continue to fall
through to the tier-5 synthesized-stub path with namespace-routed
JavaDoc URLs — IDE-resolvable, just per-file rather than centralized.
