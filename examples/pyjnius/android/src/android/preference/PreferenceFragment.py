from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferenceFragment"]

class PreferenceFragment(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/PreferenceFragment"
    __javaconstructor__ = [("()V", False)]
    TRIM_MEMORY_BACKGROUND = JavaStaticField("I")
    TRIM_MEMORY_COMPLETE = JavaStaticField("I")
    TRIM_MEMORY_MODERATE = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_CRITICAL = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_LOW = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_MODERATE = JavaStaticField("I")
    TRIM_MEMORY_UI_HIDDEN = JavaStaticField("I")
    onActivityCreated = JavaMethod("(Landroid/os/Bundle;)V")
    onViewCreated = JavaMethod("(Landroid/view/View;Landroid/os/Bundle;)V")
    onDestroyView = JavaMethod("()V")
    findPreference = JavaMethod("(Ljava/lang/CharSequence;)Landroid/preference/Preference;")
    addPreferencesFromResource = JavaMethod("(I)V")
    onPreferenceTreeClick = JavaMethod("(Landroid/preference/PreferenceScreen;Landroid/preference/Preference;)Z")
    setPreferenceScreen = JavaMethod("(Landroid/preference/PreferenceScreen;)V")
    addPreferencesFromIntent = JavaMethod("(Landroid/content/Intent;)V")
    getPreferenceManager = JavaMethod("()Landroid/preference/PreferenceManager;")
    getPreferenceScreen = JavaMethod("()Landroid/preference/PreferenceScreen;")
    onActivityResult = JavaMethod("(IILandroid/content/Intent;)V")
    onSaveInstanceState = JavaMethod("(Landroid/os/Bundle;)V")
    onCreateView = JavaMethod("(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Landroid/os/Bundle;)Landroid/view/View;")
    onCreate = JavaMethod("(Landroid/os/Bundle;)V")
    onDestroy = JavaMethod("()V")
    onStop = JavaMethod("()V")
    onStart = JavaMethod("()V")

    class OnPreferenceStartFragmentCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/preference/PreferenceFragment$OnPreferenceStartFragmentCallback"
        onPreferenceStartFragment = JavaMethod("(Landroid/preference/PreferenceFragment;Landroid/preference/Preference;)Z")