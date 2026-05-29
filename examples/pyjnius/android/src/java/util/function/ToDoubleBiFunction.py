from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ToDoubleBiFunction"]

class ToDoubleBiFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ToDoubleBiFunction"
    applyAsDouble = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)D")