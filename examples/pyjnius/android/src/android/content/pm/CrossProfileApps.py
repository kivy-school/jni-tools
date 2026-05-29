from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CrossProfileApps"]

class CrossProfileApps(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/CrossProfileApps"
    ACTION_CAN_INTERACT_ACROSS_PROFILES_CHANGED = JavaStaticField("Ljava/lang/String;")
    isProfile = JavaMethod("(Landroid/os/UserHandle;)Z")
    isManagedProfile = JavaMethod("(Landroid/os/UserHandle;)Z")
    startMainActivity = JavaMultipleMethod([("(Landroid/content/ComponentName;Landroid/os/UserHandle;)V", False, False), ("(Landroid/content/ComponentName;Landroid/os/UserHandle;Landroid/app/Activity;Landroid/os/Bundle;)V", False, False)])
    canInteractAcrossProfiles = JavaMethod("()Z")
    canRequestInteractAcrossProfiles = JavaMethod("()Z")
    createRequestInteractAcrossProfilesIntent = JavaMethod("()Landroid/content/Intent;")
    getProfileSwitchingIconDrawable = JavaMethod("(Landroid/os/UserHandle;)Landroid/graphics/drawable/Drawable;")
    getProfileSwitchingLabel = JavaMethod("(Landroid/os/UserHandle;)Ljava/lang/CharSequence;")
    getTargetUserProfiles = JavaMethod("()Ljava/util/List;")
    startActivity = JavaMultipleMethod([("(Landroid/content/Intent;Landroid/os/UserHandle;Landroid/app/Activity;Landroid/os/Bundle;)V", False, False), ("(Landroid/content/Intent;Landroid/os/UserHandle;Landroid/app/Activity;)V", False, False)])