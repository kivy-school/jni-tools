from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RatingBar"]

class RatingBar(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/RatingBar"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;)V", False)]
    setOnRatingBarChangeListener = JavaMethod("(Landroid/widget/RatingBar$OnRatingBarChangeListener;)V")
    getOnRatingBarChangeListener = JavaMethod("()Landroid/widget/RatingBar$OnRatingBarChangeListener;")
    setIsIndicator = JavaMethod("(Z)V")
    isIndicator = JavaMethod("()Z")
    setNumStars = JavaMethod("(I)V")
    getNumStars = JavaMethod("()I")
    setRating = JavaMethod("(F)V")
    getRating = JavaMethod("()F")
    setStepSize = JavaMethod("(F)V")
    getStepSize = JavaMethod("()F")
    onMeasure = JavaMethod("(II)V")
    setMax = JavaMethod("(I)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")

    class OnRatingBarChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/RatingBar/OnRatingBarChangeListener"
        onRatingChanged = JavaMethod("(Landroid/widget/RatingBar;FZ)V")