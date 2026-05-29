from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZoneRulesException"]

class ZoneRulesException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/zone/ZoneRulesException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]