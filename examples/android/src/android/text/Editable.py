from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Editable"]

class Editable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/Editable"
    replace = JavaMultipleMethod([("(IILjava/lang/CharSequence;II)Landroid/text/Editable;", False, False), ("(IILjava/lang/CharSequence;)Landroid/text/Editable;", False, False)])
    insert = JavaMultipleMethod([("(ILjava/lang/CharSequence;II)Landroid/text/Editable;", False, False), ("(ILjava/lang/CharSequence;)Landroid/text/Editable;", False, False)])
    delete = JavaMethod("(II)Landroid/text/Editable;")
    append = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Landroid/text/Editable;", False, False), ("(Ljava/lang/CharSequence;II)Landroid/text/Editable;", False, False), ("(C)Landroid/text/Editable;", False, False)])
    clear = JavaMethod("()V")
    clearSpans = JavaMethod("()V")
    setFilters = JavaMethod("([Landroid/text/InputFilter;)V")
    getFilters = JavaMethod("()[Landroid/text/InputFilter;")

    class Factory(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/Editable/Factory"
        __javaconstructor__ = [("()V", False)]
        getInstance = JavaStaticMethod("()Landroid/text/Editable$Factory;")
        newEditable = JavaMethod("(Ljava/lang/CharSequence;)Landroid/text/Editable;")