from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSSharedPreferences"]

class OSSharedPreferences(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSSharedPreferences"
    getOutcomesV2KeyName = JavaMethod("()Ljava/lang/String;")
    getPreferencesName = JavaMethod("()Ljava/lang/String;")
    getString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    saveString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    getBool = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Z)Z")
    saveBool = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Z)V")
    getInt = JavaMethod("(Ljava/lang/String;Ljava/lang/String;I)I")
    saveInt = JavaMethod("(Ljava/lang/String;Ljava/lang/String;I)V")
    getLong = JavaMethod("(Ljava/lang/String;Ljava/lang/String;J)J")
    saveLong = JavaMethod("(Ljava/lang/String;Ljava/lang/String;J)V")
    getStringSet = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Set;)Ljava/util/Set;")
    saveStringSet = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Set;)V")
    getObject = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;)Ljava/lang/Object;")
    saveObject = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;)V")