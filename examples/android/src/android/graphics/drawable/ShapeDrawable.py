from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ShapeDrawable"]

class ShapeDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/ShapeDrawable"
    __javaconstructor__ = [("()V", False), ("(Landroid/graphics/drawable/shapes/Shape;)V", False)]
    getShape = JavaMethod("()Landroid/graphics/drawable/shapes/Shape;")
    setShape = JavaMethod("(Landroid/graphics/drawable/shapes/Shape;)V")
    setShaderFactory = JavaMethod("(Landroid/graphics/drawable/ShapeDrawable$ShaderFactory;)V")
    getShaderFactory = JavaMethod("()Landroid/graphics/drawable/ShapeDrawable$ShaderFactory;")
    getPaint = JavaMethod("()Landroid/graphics/Paint;")
    setPadding = JavaMultipleMethod([("(IIII)V", False, False), ("(Landroid/graphics/Rect;)V", False, False)])
    setIntrinsicWidth = JavaMethod("(I)V")
    setIntrinsicHeight = JavaMethod("(I)V")
    getIntrinsicWidth = JavaMethod("()I")
    getIntrinsicHeight = JavaMethod("()I")
    getPadding = JavaMethod("(Landroid/graphics/Rect;)Z")
    onDraw = JavaMethod("(Landroid/graphics/drawable/shapes/Shape;Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getChangingConfigurations = JavaMethod("()I")
    setAlpha = JavaMethod("(I)V")
    getAlpha = JavaMethod("()I")
    setTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    setTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    setColorFilter = JavaMethod("(Landroid/graphics/ColorFilter;)V")
    getOpacity = JavaMethod("()I")
    setDither = JavaMethod("(Z)V")
    onBoundsChange = JavaMethod("(Landroid/graphics/Rect;)V")
    onStateChange = JavaMethod("([I)Z")
    isStateful = JavaMethod("()Z")
    hasFocusStateSpecified = JavaMethod("()Z")
    inflateTag = JavaMethod("(Ljava/lang/String;Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;)Z")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")
    getConstantState = JavaMethod("()Landroid/graphics/drawable/Drawable$ConstantState;")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")

    class ShaderFactory(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/drawable/ShapeDrawable/ShaderFactory"
        __javaconstructor__ = [("()V", False)]
        resize = JavaMethod("(II)Landroid/graphics/Shader;")