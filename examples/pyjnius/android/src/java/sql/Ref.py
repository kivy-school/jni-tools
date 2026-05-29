from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Ref"]

class Ref(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Ref"
    getObject = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(Ljava/util/Map;)Ljava/lang/Object;", False, False)])
    getBaseTypeName = JavaMethod("()Ljava/lang/String;")
    setObject = JavaMethod("(Ljava/lang/Object;)V")