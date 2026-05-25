from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    getWeight = JavaMethod("()I")
    getStyle = JavaMethod("()I")
    isBold = JavaMethod("()Z")
    isItalic = JavaMethod("()Z")
    getSystemFontFamilyName = JavaMethod("()Ljava/lang/String;")
    create = JavaMultipleMethod([("(Ljava/lang/String;I)Landroid/graphics/Typeface;", True, False), ("(Landroid/graphics/Typeface;I)Landroid/graphics/Typeface;", True, False), ("(Landroid/graphics/Typeface;IZ)Landroid/graphics/Typeface;", True, False)])
    defaultFromStyle = JavaStaticMethod("(I)Landroid/graphics/Typeface;")
    createFromAsset = JavaStaticMethod("(Landroid/content/res/AssetManager;Ljava/lang/String;)Landroid/graphics/Typeface;")
    createFromFile = JavaMultipleMethod([("(Ljava/io/File;)Landroid/graphics/Typeface;", True, False), ("(Ljava/lang/String;)Landroid/graphics/Typeface;", True, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/Typeface/Builder"
        __javaconstructor__ = [("(Ljava/io/File;)V", False), ("(Ljava/io/FileDescriptor;)V", False), ("(Ljava/lang/String;)V", False), ("(Landroid/content/res/AssetManager;Ljava/lang/String;)V", False)]
        setWeight = JavaMethod("(I)Landroid/graphics/Typeface$Builder;")
        setItalic = JavaMethod("(Z)Landroid/graphics/Typeface$Builder;")
        setTtcIndex = JavaMethod("(I)Landroid/graphics/Typeface$Builder;")
        setFontVariationSettings = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/graphics/Typeface$Builder;", False, False), ("([Landroid/graphics/fonts/FontVariationAxis;)Landroid/graphics/Typeface$Builder;", False, False)])
        setFallback = JavaMethod("(Ljava/lang/String;)Landroid/graphics/Typeface$Builder;")
        build = JavaMethod("()Landroid/graphics/Typeface;")

    class CustomFallbackBuilder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/Typeface/CustomFallbackBuilder"
        __javaconstructor__ = [("(Landroid/graphics/fonts/FontFamily;)V", False)]
        getMaxCustomFallbackCount = JavaStaticMethod("()I")
        setSystemFallback = JavaMethod("(Ljava/lang/String;)Landroid/graphics/Typeface$CustomFallbackBuilder;")
        setStyle = JavaMethod("(Landroid/graphics/fonts/FontStyle;)Landroid/graphics/Typeface$CustomFallbackBuilder;")
        addCustomFallback = JavaMethod("(Landroid/graphics/fonts/FontFamily;)Landroid/graphics/Typeface$CustomFallbackBuilder;")
        build = JavaMethod("()Landroid/graphics/Typeface;")