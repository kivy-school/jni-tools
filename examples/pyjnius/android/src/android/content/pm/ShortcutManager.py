from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ShortcutManager"]

class ShortcutManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ShortcutManager"
    FLAG_MATCH_CACHED = JavaStaticField("I")
    FLAG_MATCH_DYNAMIC = JavaStaticField("I")
    FLAG_MATCH_MANIFEST = JavaStaticField("I")
    FLAG_MATCH_PINNED = JavaStaticField("I")
    addDynamicShortcuts = JavaMethod("(Ljava/util/List;)Z")
    disableShortcuts = JavaMultipleMethod([("(Ljava/util/List;)V", False, False), ("(Ljava/util/List;Ljava/lang/CharSequence;)V", False, False)])
    createShortcutResultIntent = JavaMethod("(Landroid/content/pm/ShortcutInfo;)Landroid/content/Intent;")
    enableShortcuts = JavaMethod("(Ljava/util/List;)V")
    getDynamicShortcuts = JavaMethod("()Ljava/util/List;")
    getIconMaxHeight = JavaMethod("()I")
    getIconMaxWidth = JavaMethod("()I")
    getManifestShortcuts = JavaMethod("()Ljava/util/List;")
    getMaxShortcutCountPerActivity = JavaMethod("()I")
    getPinnedShortcuts = JavaMethod("()Ljava/util/List;")
    getShortcuts = JavaMethod("(I)Ljava/util/List;")
    isRateLimitingActive = JavaMethod("()Z")
    reportShortcutUsed = JavaMethod("(Ljava/lang/String;)V")
    isRequestPinShortcutSupported = JavaMethod("()Z")
    pushDynamicShortcut = JavaMethod("(Landroid/content/pm/ShortcutInfo;)V")
    removeAllDynamicShortcuts = JavaMethod("()V")
    removeDynamicShortcuts = JavaMethod("(Ljava/util/List;)V")
    removeLongLivedShortcuts = JavaMethod("(Ljava/util/List;)V")
    requestPinShortcut = JavaMethod("(Landroid/content/pm/ShortcutInfo;Landroid/content/IntentSender;)Z")
    setDynamicShortcuts = JavaMethod("(Ljava/util/List;)Z")
    updateShortcuts = JavaMethod("(Ljava/util/List;)Z")