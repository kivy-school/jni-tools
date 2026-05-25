from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharacterData"]

class CharacterData(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/CharacterData"
    getData = JavaMethod("()Ljava/lang/String;")
    setData = JavaMethod("(Ljava/lang/String;)V")
    getLength = JavaMethod("()I")
    substringData = JavaMethod("(II)Ljava/lang/String;")
    appendData = JavaMethod("(Ljava/lang/String;)V")
    insertData = JavaMethod("(ILjava/lang/String;)V")
    deleteData = JavaMethod("(II)V")
    replaceData = JavaMethod("(IILjava/lang/String;)V")