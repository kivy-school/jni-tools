from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Validators"]

class Validators(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/Validators"
    and = JavaStaticMethod("([Landroid/service/autofill/Validator;)Landroid/service/autofill/Validator;", varargs=True)
    or = JavaStaticMethod("([Landroid/service/autofill/Validator;)Landroid/service/autofill/Validator;", varargs=True)
    not = JavaStaticMethod("(Landroid/service/autofill/Validator;)Landroid/service/autofill/Validator;")