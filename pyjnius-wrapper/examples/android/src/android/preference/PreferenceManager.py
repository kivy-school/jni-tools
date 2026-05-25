from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferenceManager"]

class PreferenceManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/PreferenceManager"
    KEY_HAS_SET_DEFAULT_VALUES = JavaStaticField("Ljava/lang/String;")
    METADATA_KEY_PREFERENCES = JavaStaticField("Ljava/lang/String;")
    setPreferenceDataStore = JavaMethod("(Landroid/preference/PreferenceDataStore;)V")
    getPreferenceDataStore = JavaMethod("()Landroid/preference/PreferenceDataStore;")
    createPreferenceScreen = JavaMethod("(Landroid/content/Context;)Landroid/preference/PreferenceScreen;")
    getSharedPreferencesName = JavaMethod("()Ljava/lang/String;")
    setSharedPreferencesName = JavaMethod("(Ljava/lang/String;)V")
    getSharedPreferencesMode = JavaMethod("()I")
    setSharedPreferencesMode = JavaMethod("(I)V")
    setStorageDefault = JavaMethod("()V")
    setStorageDeviceProtected = JavaMethod("()V")
    isStorageDefault = JavaMethod("()Z")
    isStorageDeviceProtected = JavaMethod("()Z")
    getSharedPreferences = JavaMethod("()Landroid/content/SharedPreferences;")
    getDefaultSharedPreferences = JavaStaticMethod("(Landroid/content/Context;)Landroid/content/SharedPreferences;")
    getDefaultSharedPreferencesName = JavaStaticMethod("(Landroid/content/Context;)Ljava/lang/String;")
    findPreference = JavaMethod("(Ljava/lang/CharSequence;)Landroid/preference/Preference;")
    setDefaultValues = JavaMultipleMethod([("(Landroid/content/Context;IZ)V", True, False), ("(Landroid/content/Context;Ljava/lang/String;IIZ)V", True, False)])

    class OnActivityDestroyListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/preference/PreferenceManager/OnActivityDestroyListener"
        onActivityDestroy = JavaMethod("()V")

    class OnActivityResultListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/preference/PreferenceManager/OnActivityResultListener"
        onActivityResult = JavaMethod("(IILandroid/content/Intent;)Z")

    class OnActivityStopListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/preference/PreferenceManager/OnActivityStopListener"
        onActivityStop = JavaMethod("()V")