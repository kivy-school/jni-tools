from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Highlights"]

class Highlights(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/Highlights"
    getSize = JavaMethod("()I")
    getPaint = JavaMethod("(I)Landroid/graphics/Paint;")
    getRanges = JavaMethod("(I)[I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/Highlights$Builder"
        __javaconstructor__ = [("()V", False)]
        addRange = JavaMethod("(Landroid/graphics/Paint;II)Landroid/text/Highlights$Builder;")
        addRanges = JavaMethod("(Landroid/graphics/Paint;[I)Landroid/text/Highlights$Builder;", varargs=True)
        build = JavaMethod("()Landroid/text/Highlights;")