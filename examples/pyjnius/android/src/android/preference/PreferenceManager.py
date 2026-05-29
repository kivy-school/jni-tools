from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferenceManager"]

class PreferenceManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/PreferenceManager"
    KEY_HAS_SET_DEFAULT_VALUES = JavaStaticField("Ljava/lang/String;")
    METADATA_KEY_PREFERENCES = JavaStaticField("Ljava/lang/String;")
    createPreferenceScreen = JavaMethod("(Landroid/content/Context;)Landroid/preference/PreferenceScreen;")
    findPreference = JavaMethod("(Ljava/lang/CharSequence;)Landroid/preference/Preference;")
    setDefaultValues = JavaMultipleMethod([("(Landroid/content/Context;Ljava/lang/String;IIZ)V", True, False), ("(Landroid/content/Context;IZ)V", True, False)])
    isStorageDefault = JavaMethod("()Z")
    getDefaultSharedPreferencesName = JavaStaticMethod("(Landroid/content/Context;)Ljava/lang/String;")
    getSharedPreferencesMode = JavaMethod("()I")
    getSharedPreferencesName = JavaMethod("()Ljava/lang/String;")
    isStorageDeviceProtected = JavaMethod("()Z")
    setSharedPreferencesMode = JavaMethod("(I)V")
    setSharedPreferencesName = JavaMethod("(Ljava/lang/String;)V")
    setStorageDefault = JavaMethod("()V")
    setStorageDeviceProtected = JavaMethod("()V")
    setPreferenceDataStore = JavaMethod("(Landroid/preference/PreferenceDataStore;)V")
    getSharedPreferences = JavaMethod("()Landroid/content/SharedPreferences;")
    getPreferenceDataStore = JavaMethod("()Landroid/preference/PreferenceDataStore;")
    getDefaultSharedPreferences = JavaStaticMethod("(Landroid/content/Context;)Landroid/content/SharedPreferences;")

    class OnActivityStopListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/preference/PreferenceManager$OnActivityStopListener"
        onActivityStop = JavaMethod("()V")

    class OnActivityResultListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/preference/PreferenceManager$OnActivityResultListener"
        onActivityResult = JavaMethod("(IILandroid/content/Intent;)Z")

    class OnActivityDestroyListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/preference/PreferenceManager$OnActivityDestroyListener"
        onActivityDestroy = JavaMethod("()V")