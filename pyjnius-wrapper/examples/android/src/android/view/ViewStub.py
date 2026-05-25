from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewStub"]

class ViewStub(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ViewStub"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    getInflatedId = JavaMethod("()I")
    setInflatedId = JavaMethod("(I)V")
    getLayoutResource = JavaMethod("()I")
    setLayoutResource = JavaMethod("(I)V")
    setLayoutInflater = JavaMethod("(Landroid/view/LayoutInflater;)V")
    getLayoutInflater = JavaMethod("()Landroid/view/LayoutInflater;")
    onMeasure = JavaMethod("(II)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    dispatchDraw = JavaMethod("(Landroid/graphics/Canvas;)V")
    setVisibility = JavaMethod("(I)V")
    inflate = JavaMethod("()Landroid/view/View;")
    setOnInflateListener = JavaMethod("(Landroid/view/ViewStub$OnInflateListener;)V")

    class OnInflateListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewStub/OnInflateListener"
        onInflate = JavaMethod("(Landroid/view/ViewStub;Landroid/view/View;)V")