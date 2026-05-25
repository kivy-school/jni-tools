from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CrossProfileApps"]

class CrossProfileApps(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/CrossProfileApps"
    ACTION_CAN_INTERACT_ACROSS_PROFILES_CHANGED = JavaStaticField("Ljava/lang/String;")
    startMainActivity = JavaMultipleMethod([("(Landroid/content/ComponentName;Landroid/os/UserHandle;)V", False, False), ("(Landroid/content/ComponentName;Landroid/os/UserHandle;Landroid/app/Activity;Landroid/os/Bundle;)V", False, False)])
    startActivity = JavaMultipleMethod([("(Landroid/content/Intent;Landroid/os/UserHandle;Landroid/app/Activity;)V", False, False), ("(Landroid/content/Intent;Landroid/os/UserHandle;Landroid/app/Activity;Landroid/os/Bundle;)V", False, False)])
    getTargetUserProfiles = JavaMethod("()Ljava/util/List;")
    isProfile = JavaMethod("(Landroid/os/UserHandle;)Z")
    isManagedProfile = JavaMethod("(Landroid/os/UserHandle;)Z")
    getProfileSwitchingLabel = JavaMethod("(Landroid/os/UserHandle;)Ljava/lang/CharSequence;")
    getProfileSwitchingIconDrawable = JavaMethod("(Landroid/os/UserHandle;)Landroid/graphics/drawable/Drawable;")
    canRequestInteractAcrossProfiles = JavaMethod("()Z")
    canInteractAcrossProfiles = JavaMethod("()Z")
    createRequestInteractAcrossProfilesIntent = JavaMethod("()Landroid/content/Intent;")