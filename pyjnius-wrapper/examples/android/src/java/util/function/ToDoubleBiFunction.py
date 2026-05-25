from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ToDoubleBiFunction"]

class ToDoubleBiFunction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ToDoubleBiFunction"
    applyAsDouble = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)D")