from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyChangeEvent"]

class PropertyChangeEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/beans/PropertyChangeEvent"
    __javaconstructor__ = [("(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V", False)]
    getNewValue = JavaMethod("()Ljava/lang/Object;")
    toString = JavaMethod("()Ljava/lang/String;")
    getPropertyName = JavaMethod("()Ljava/lang/String;")
    getOldValue = JavaMethod("()Ljava/lang/Object;")
    getPropagationId = JavaMethod("()Ljava/lang/Object;")
    setPropagationId = JavaMethod("(Ljava/lang/Object;)V")