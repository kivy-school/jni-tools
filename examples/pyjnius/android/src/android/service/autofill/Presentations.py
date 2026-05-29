from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Presentations"]

class Presentations(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/Presentations"
    getInlinePresentation = JavaMethod("()Landroid/service/autofill/InlinePresentation;")
    getInlineTooltipPresentation = JavaMethod("()Landroid/service/autofill/InlinePresentation;")
    getMenuPresentation = JavaMethod("()Landroid/widget/RemoteViews;")
    getDialogPresentation = JavaMethod("()Landroid/widget/RemoteViews;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/Presentations$Builder"
        __javaconstructor__ = [("()V", False)]
        setInlinePresentation = JavaMethod("(Landroid/service/autofill/InlinePresentation;)Landroid/service/autofill/Presentations$Builder;")
        setDialogPresentation = JavaMethod("(Landroid/widget/RemoteViews;)Landroid/service/autofill/Presentations$Builder;")
        setInlineTooltipPresentation = JavaMethod("(Landroid/service/autofill/InlinePresentation;)Landroid/service/autofill/Presentations$Builder;")
        setMenuPresentation = JavaMethod("(Landroid/widget/RemoteViews;)Landroid/service/autofill/Presentations$Builder;")
        build = JavaMethod("()Landroid/service/autofill/Presentations;")