from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ShapeDrawable"]

class ShapeDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/ShapeDrawable"
    __javaconstructor__ = [("()V", False), ("(Landroid/graphics/drawable/shapes/Shape;)V", False)]
    getShape = JavaMethod("()Landroid/graphics/drawable/shapes/Shape;")
    setShaderFactory = JavaMethod("(Landroid/graphics/drawable/ShapeDrawable$ShaderFactory;)V")
    setIntrinsicHeight = JavaMethod("(I)V")
    getShaderFactory = JavaMethod("()Landroid/graphics/drawable/ShapeDrawable$ShaderFactory;")
    setIntrinsicWidth = JavaMethod("(I)V")
    setShape = JavaMethod("(Landroid/graphics/drawable/shapes/Shape;)V")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    setAlpha = JavaMethod("(I)V")
    setColorFilter = JavaMethod("(Landroid/graphics/ColorFilter;)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getAlpha = JavaMethod("()I")
    setPadding = JavaMultipleMethod([("(IIII)V", False, False), ("(Landroid/graphics/Rect;)V", False, False)])
    getPaint = JavaMethod("()Landroid/graphics/Paint;")
    getChangingConfigurations = JavaMethod("()I")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    getConstantState = JavaMethod("()Landroid/graphics/drawable/Drawable$ConstantState;")
    getIntrinsicHeight = JavaMethod("()I")
    getIntrinsicWidth = JavaMethod("()I")
    getOpacity = JavaMethod("()I")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")
    getPadding = JavaMethod("(Landroid/graphics/Rect;)Z")
    hasFocusStateSpecified = JavaMethod("()Z")
    isStateful = JavaMethod("()Z")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setDither = JavaMethod("(Z)V")
    setTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    setTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")

    class ShaderFactory(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/drawable/ShapeDrawable$ShaderFactory"
        __javaconstructor__ = [("()V", False)]
        resize = JavaMethod("(II)Landroid/graphics/Shader;")