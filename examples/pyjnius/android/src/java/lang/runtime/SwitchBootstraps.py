from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SwitchBootstraps"]

class SwitchBootstraps(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/runtime/SwitchBootstraps"
    typeSwitch = JavaStaticMethod("(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite;", varargs=True)
    enumSwitch = JavaStaticMethod("(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite;", varargs=True)