from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyChangeEvent"]

class PropertyChangeEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/beans/PropertyChangeEvent"
    __javaconstructor__ = [("(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V", False)]
    getPropertyName = JavaMethod("()Ljava/lang/String;")
    getNewValue = JavaMethod("()Ljava/lang/Object;")
    getOldValue = JavaMethod("()Ljava/lang/Object;")
    setPropagationId = JavaMethod("(Ljava/lang/Object;)V")
    getPropagationId = JavaMethod("()Ljava/lang/Object;")
    toString = JavaMethod("()Ljava/lang/String;")