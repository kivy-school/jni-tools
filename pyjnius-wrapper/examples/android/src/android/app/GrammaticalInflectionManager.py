from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GrammaticalInflectionManager"]

class GrammaticalInflectionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/GrammaticalInflectionManager"
    getApplicationGrammaticalGender = JavaMethod("()I")
    setRequestedApplicationGrammaticalGender = JavaMethod("(I)V")
    getSystemGrammaticalGender = JavaMethod("()I")