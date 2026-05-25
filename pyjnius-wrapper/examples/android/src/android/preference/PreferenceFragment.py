from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferenceFragment"]

class PreferenceFragment(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/PreferenceFragment"
    __javaconstructor__ = [("()V", False)]
    onCreate = JavaMethod("(Landroid/os/Bundle;)V")
    onCreateView = JavaMethod("(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Landroid/os/Bundle;)Landroid/view/View;")
    onViewCreated = JavaMethod("(Landroid/view/View;Landroid/os/Bundle;)V")
    onActivityCreated = JavaMethod("(Landroid/os/Bundle;)V")
    onStart = JavaMethod("()V")
    onStop = JavaMethod("()V")
    onDestroyView = JavaMethod("()V")
    onDestroy = JavaMethod("()V")
    onSaveInstanceState = JavaMethod("(Landroid/os/Bundle;)V")
    onActivityResult = JavaMethod("(IILandroid/content/Intent;)V")
    getPreferenceManager = JavaMethod("()Landroid/preference/PreferenceManager;")
    setPreferenceScreen = JavaMethod("(Landroid/preference/PreferenceScreen;)V")
    getPreferenceScreen = JavaMethod("()Landroid/preference/PreferenceScreen;")
    addPreferencesFromIntent = JavaMethod("(Landroid/content/Intent;)V")
    addPreferencesFromResource = JavaMethod("(I)V")
    onPreferenceTreeClick = JavaMethod("(Landroid/preference/PreferenceScreen;Landroid/preference/Preference;)Z")
    findPreference = JavaMethod("(Ljava/lang/CharSequence;)Landroid/preference/Preference;")

    class OnPreferenceStartFragmentCallback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/preference/PreferenceFragment/OnPreferenceStartFragmentCallback"
        onPreferenceStartFragment = JavaMethod("(Landroid/preference/PreferenceFragment;Landroid/preference/Preference;)Z")