from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Typeface"]

class Typeface(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Typeface"
    BOLD = JavaStaticField("I")
    BOLD_ITALIC = JavaStaticField("I")
    DEFAULT = JavaStaticField("Landroid/graphics/Typeface;")
    DEFAULT_BOLD = JavaStaticField("Landroid/graphics/Typeface;")
    ITALIC = JavaStaticField("I")
    MONOSPACE = JavaStaticField("Landroid/graphics/Typeface;")
    NORMAL = JavaStaticField("I")
    SANS_SERIF = JavaStaticField("Landroid/graphics/Typeface;")
    SERIF = JavaStaticField("Landroid/graphics/Typeface;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    create = JavaMultipleMethod([("(Landroid/graphics/Typeface;I)Landroid/graphics/Typeface;", True, False), ("(Landroid/graphics/Typeface;IZ)Landroid/graphics/Typeface;", True, False), ("(Ljava/lang/String;I)Landroid/graphics/Typeface;", True, False)])
    getWeight = JavaMethod("()I")
    isItalic = JavaMethod("()Z")
    getSystemFontFamilyName = JavaMethod("()Ljava/lang/String;")
    isBold = JavaMethod("()Z")
    createFromAsset = JavaStaticMethod("(Landroid/content/res/AssetManager;Ljava/lang/String;)Landroid/graphics/Typeface;")
    createFromFile = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/graphics/Typeface;", True, False), ("(Ljava/io/File;)Landroid/graphics/Typeface;", True, False)])
    defaultFromStyle = JavaStaticMethod("(I)Landroid/graphics/Typeface;")
    getStyle = JavaMethod("()I")

    class CustomFallbackBuilder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/Typeface$CustomFallbackBuilder"
        __javaconstructor__ = [("(Landroid/graphics/fonts/FontFamily;)V", False)]
        setSystemFallback = JavaMethod("(Ljava/lang/String;)Landroid/graphics/Typeface$CustomFallbackBuilder;")
        addCustomFallback = JavaMethod("(Landroid/graphics/fonts/FontFamily;)Landroid/graphics/Typeface$CustomFallbackBuilder;")
        getMaxCustomFallbackCount = JavaStaticMethod("()I")
        build = JavaMethod("()Landroid/graphics/Typeface;")
        setStyle = JavaMethod("(Landroid/graphics/fonts/FontStyle;)Landroid/graphics/Typeface$CustomFallbackBuilder;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/Typeface$Builder"
        __javaconstructor__ = [("(Ljava/io/FileDescriptor;)V", False), ("(Ljava/io/File;)V", False), ("(Ljava/lang/String;)V", False), ("(Landroid/content/res/AssetManager;Ljava/lang/String;)V", False)]
        setTtcIndex = JavaMethod("(I)Landroid/graphics/Typeface$Builder;")
        setFallback = JavaMethod("(Ljava/lang/String;)Landroid/graphics/Typeface$Builder;")
        setItalic = JavaMethod("(Z)Landroid/graphics/Typeface$Builder;")
        setWeight = JavaMethod("(I)Landroid/graphics/Typeface$Builder;")
        build = JavaMethod("()Landroid/graphics/Typeface;")
        setFontVariationSettings = JavaMultipleMethod([("([Landroid/graphics/fonts/FontVariationAxis;)Landroid/graphics/Typeface$Builder;", False, False), ("(Ljava/lang/String;)Landroid/graphics/Typeface$Builder;", False, False)])