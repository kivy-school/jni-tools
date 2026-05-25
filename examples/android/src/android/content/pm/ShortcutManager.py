from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ShortcutManager"]

class ShortcutManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ShortcutManager"
    FLAG_MATCH_CACHED = JavaStaticField("I")
    FLAG_MATCH_DYNAMIC = JavaStaticField("I")
    FLAG_MATCH_MANIFEST = JavaStaticField("I")
    FLAG_MATCH_PINNED = JavaStaticField("I")
    setDynamicShortcuts = JavaMethod("(Ljava/util/List;)Z")
    getDynamicShortcuts = JavaMethod("()Ljava/util/List;")
    getManifestShortcuts = JavaMethod("()Ljava/util/List;")
    getShortcuts = JavaMethod("(I)Ljava/util/List;")
    addDynamicShortcuts = JavaMethod("(Ljava/util/List;)Z")
    removeDynamicShortcuts = JavaMethod("(Ljava/util/List;)V")
    removeAllDynamicShortcuts = JavaMethod("()V")
    removeLongLivedShortcuts = JavaMethod("(Ljava/util/List;)V")
    getPinnedShortcuts = JavaMethod("()Ljava/util/List;")
    updateShortcuts = JavaMethod("(Ljava/util/List;)Z")
    disableShortcuts = JavaMultipleMethod([("(Ljava/util/List;)V", False, False), ("(Ljava/util/List;Ljava/lang/CharSequence;)V", False, False)])
    enableShortcuts = JavaMethod("(Ljava/util/List;)V")
    getMaxShortcutCountPerActivity = JavaMethod("()I")
    isRateLimitingActive = JavaMethod("()Z")
    getIconMaxWidth = JavaMethod("()I")
    getIconMaxHeight = JavaMethod("()I")
    reportShortcutUsed = JavaMethod("(Ljava/lang/String;)V")
    isRequestPinShortcutSupported = JavaMethod("()Z")
    requestPinShortcut = JavaMethod("(Landroid/content/pm/ShortcutInfo;Landroid/content/IntentSender;)Z")
    createShortcutResultIntent = JavaMethod("(Landroid/content/pm/ShortcutInfo;)Landroid/content/Intent;")
    pushDynamicShortcut = JavaMethod("(Landroid/content/pm/ShortcutInfo;)V")