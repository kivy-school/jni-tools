from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IndexedPropertyChangeEvent"]

class IndexedPropertyChangeEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/beans/IndexedPropertyChangeEvent"
    __javaconstructor__ = [("(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;I)V", False)]
    getIndex = JavaMethod("()I")