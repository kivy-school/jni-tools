from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferenceDataStore"]

class PreferenceDataStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/PreferenceDataStore"
    getStringSet = JavaMethod("(Ljava/lang/String;Ljava/util/Set;)Ljava/util/Set;")
    getBoolean = JavaMethod("(Ljava/lang/String;Z)Z")
    putBoolean = JavaMethod("(Ljava/lang/String;Z)V")
    getInt = JavaMethod("(Ljava/lang/String;I)I")
    putInt = JavaMethod("(Ljava/lang/String;I)V")
    getLong = JavaMethod("(Ljava/lang/String;J)J")
    putLong = JavaMethod("(Ljava/lang/String;J)V")
    getFloat = JavaMethod("(Ljava/lang/String;F)F")
    putFloat = JavaMethod("(Ljava/lang/String;F)V")
    putStringSet = JavaMethod("(Ljava/lang/String;Ljava/util/Set;)V")
    getString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    putString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")