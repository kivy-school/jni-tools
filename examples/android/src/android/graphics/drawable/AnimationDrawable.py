from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnimationDrawable"]

class AnimationDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/AnimationDrawable"
    __javaconstructor__ = [("()V", False)]
    setVisible = JavaMethod("(ZZ)Z")
    start = JavaMethod("()V")
    stop = JavaMethod("()V")
    isRunning = JavaMethod("()Z")
    run = JavaMethod("()V")
    unscheduleSelf = JavaMethod("(Ljava/lang/Runnable;)V")
    getNumberOfFrames = JavaMethod("()I")
    getFrame = JavaMethod("(I)Landroid/graphics/drawable/Drawable;")
    getDuration = JavaMethod("(I)I")
    isOneShot = JavaMethod("()Z")
    setOneShot = JavaMethod("(Z)V")
    addFrame = JavaMethod("(Landroid/graphics/drawable/Drawable;I)V")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setConstantState = JavaMethod("(Landroid/graphics/drawable/DrawableContainer$DrawableContainerState;)V")