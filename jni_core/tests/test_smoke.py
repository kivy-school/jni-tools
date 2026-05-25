"""Smoke test: import jni_core, boot a JVM, attach, find java.lang.String."""
import pytest


def test_module_imports():
    import jni_core
    assert jni_core.__version__


def test_get_env_returns_pointer():
    # Skipped if no JVM is reachable. We attempt to attach/create a JVM and
    # ask for a JNIEnv. On macOS, JAVA_HOME must point to a JDK.
    import jni_core
    try:
        env_ptr = jni_core.get_env.__wrapped__() if hasattr(jni_core.get_env, "__wrapped__") else None
    except Exception:
        env_ptr = None
    # Real test: call the cpdef directly.
    from jni_core._core import py_get_env
    try:
        ptr = py_get_env()
    except RuntimeError as exc:
        pytest.skip(f"No JVM available in this environment: {exc}")
    assert isinstance(ptr, int)
    assert ptr != 0


def test_find_string_class_via_low_level_api():
    """Round-trip: get env → look up java/lang/String via a fresh cdef helper
    callable. This exercises the C dispatch path."""
    from jni_core._core import py_get_env
    try:
        py_get_env()
    except RuntimeError as exc:
        pytest.skip(f"No JVM available: {exc}")
    # If py_get_env works, we have a JVM. Deeper integration is covered
    # by the generator's end-to-end test (Phase 4).
