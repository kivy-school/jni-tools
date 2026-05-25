from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Presentations"]

class Presentations(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/Presentations"
    getMenuPresentation = JavaMethod("()Landroid/widget/RemoteViews;")
    getInlinePresentation = JavaMethod("()Landroid/service/autofill/InlinePresentation;")
    getDialogPresentation = JavaMethod("()Landroid/widget/RemoteViews;")
    getInlineTooltipPresentation = JavaMethod("()Landroid/service/autofill/InlinePresentation;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/Presentations/Builder"
        __javaconstructor__ = [("()V", False)]
        setMenuPresentation = JavaMethod("(Landroid/widget/RemoteViews;)Landroid/service/autofill/Presentations$Builder;")
        setInlinePresentation = JavaMethod("(Landroid/service/autofill/InlinePresentation;)Landroid/service/autofill/Presentations$Builder;")
        setDialogPresentation = JavaMethod("(Landroid/widget/RemoteViews;)Landroid/service/autofill/Presentations$Builder;")
        setInlineTooltipPresentation = JavaMethod("(Landroid/service/autofill/InlinePresentation;)Landroid/service/autofill/Presentations$Builder;")
        build = JavaMethod("()Landroid/service/autofill/Presentations;")