from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BundleCompat"]

class BundleCompat(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/BundleCompat"
    putString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    putInt = JavaMethod("(Ljava/lang/String;Ljava/lang/Integer;)V")
    putLong = JavaMethod("(Ljava/lang/String;Ljava/lang/Long;)V")
    putBoolean = JavaMethod("(Ljava/lang/String;Ljava/lang/Boolean;)V")
    getString = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getInt = JavaMethod("(Ljava/lang/String;)Ljava/lang/Integer;")
    getLong = JavaMethod("(Ljava/lang/String;)Ljava/lang/Long;")
    getBoolean = JavaMultipleMethod([("(Ljava/lang/String;)Z", False, False), ("(Ljava/lang/String;Z)Z", False, False)])
    containsKey = JavaMethod("(Ljava/lang/String;)Z")
    getBundle = JavaMethod("()Ljava/lang/Object;")
    setBundle = JavaMethod("(Landroid/os/Parcelable;)V")