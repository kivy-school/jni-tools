from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Field"]

class Field(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/Field"
    getPresentations = JavaMethod("()Landroid/service/autofill/Presentations;")
    getValue = JavaMethod("()Landroid/view/autofill/AutofillValue;")
    getFilter = JavaMethod("()Ljava/util/regex/Pattern;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/Field$Builder"
        __javaconstructor__ = [("()V", False)]
        setPresentations = JavaMethod("(Landroid/service/autofill/Presentations;)Landroid/service/autofill/Field$Builder;")
        setValue = JavaMethod("(Landroid/view/autofill/AutofillValue;)Landroid/service/autofill/Field$Builder;")
        build = JavaMethod("()Landroid/service/autofill/Field;")
        setFilter = JavaMethod("(Ljava/util/regex/Pattern;)Landroid/service/autofill/Field$Builder;")