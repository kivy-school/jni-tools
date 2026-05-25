from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferenceDataStore"]

class PreferenceDataStore(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/PreferenceDataStore"
    putString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    putStringSet = JavaMethod("(Ljava/lang/String;Ljava/util/Set;)V")
    putInt = JavaMethod("(Ljava/lang/String;I)V")
    putLong = JavaMethod("(Ljava/lang/String;J)V")
    putFloat = JavaMethod("(Ljava/lang/String;F)V")
    putBoolean = JavaMethod("(Ljava/lang/String;Z)V")
    getString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    getStringSet = JavaMethod("(Ljava/lang/String;Ljava/util/Set;)Ljava/util/Set;")
    getInt = JavaMethod("(Ljava/lang/String;I)I")
    getLong = JavaMethod("(Ljava/lang/String;J)J")
    getFloat = JavaMethod("(Ljava/lang/String;F)F")
    getBoolean = JavaMethod("(Ljava/lang/String;Z)Z")