from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppSetId"]

class AppSetId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/appsetid/AppSetId"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False)]
    SCOPE_APP = JavaStaticField("I")
    SCOPE_DEVELOPER = JavaStaticField("I")
    getId = JavaMethod("()Ljava/lang/String;")
    getScope = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")