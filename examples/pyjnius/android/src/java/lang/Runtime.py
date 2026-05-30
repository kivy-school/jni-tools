from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class SwitchBootstraps(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/runtime/SwitchBootstraps"
    enumSwitch = JavaStaticMethod("(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite;", varargs=True)
    typeSwitch = JavaStaticMethod("(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite;", varargs=True)

class ObjectMethods(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/runtime/ObjectMethods"
    bootstrap = JavaStaticMethod("(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/TypeDescriptor;Ljava/lang/Class;Ljava/lang/String;[Ljava/lang/invoke/MethodHandle;)Ljava/lang/Object;", varargs=True)