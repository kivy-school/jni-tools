from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnimationDrawable"]

class AnimationDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/AnimationDrawable"
    __javaconstructor__ = [("()V", False)]
    isOneShot = JavaMethod("()Z")
    getNumberOfFrames = JavaMethod("()I")
    setOneShot = JavaMethod("(Z)V")
    run = JavaMethod("()V")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    start = JavaMethod("()V")
    getFrame = JavaMethod("(I)Landroid/graphics/drawable/Drawable;")
    getDuration = JavaMethod("(I)I")
    stop = JavaMethod("()V")
    isRunning = JavaMethod("()Z")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setVisible = JavaMethod("(ZZ)Z")
    unscheduleSelf = JavaMethod("(Ljava/lang/Runnable;)V")
    addFrame = JavaMethod("(Landroid/graphics/drawable/Drawable;I)V")