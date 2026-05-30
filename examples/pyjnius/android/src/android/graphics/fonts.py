from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class FontFamily(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/fonts/FontFamily"
    getFont = JavaMethod("(I)Landroid/graphics/fonts/Font;")
    getSize = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/fonts/FontFamily$Builder"
        __javaconstructor__ = [("(Landroid/graphics/fonts/Font;)V", False)]
        buildVariableFamily = JavaMethod("()Landroid/graphics/fonts/FontFamily;")
        addFont = JavaMethod("(Landroid/graphics/fonts/Font;)Landroid/graphics/fonts/FontFamily$Builder;")
        build = JavaMethod("()Landroid/graphics/fonts/FontFamily;")

class Font(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/fonts/Font"
    getBuffer = JavaMethod("()Ljava/nio/ByteBuffer;")
    getAxes = JavaMethod("()[Landroid/graphics/fonts/FontVariationAxis;")
    getTtcIndex = JavaMethod("()I")
    getGlyphBounds = JavaMethod("(ILandroid/graphics/Paint;Landroid/graphics/RectF;)F")
    getLocaleList = JavaMethod("()Landroid/os/LocaleList;")
    getSourceIdentifier = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getStyle = JavaMethod("()Landroid/graphics/fonts/FontStyle;")
    getMetrics = JavaMethod("(Landroid/graphics/Paint;Landroid/graphics/Paint$FontMetrics;)V")
    getFile = JavaMethod("()Ljava/io/File;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/fonts/Font$Builder"
        __javaconstructor__ = [("(Landroid/content/res/AssetManager;Ljava/lang/String;)V", False), ("(Ljava/nio/ByteBuffer;)V", False), ("(Ljava/io/File;)V", False), ("(Landroid/graphics/fonts/Font;)V", False), ("(Landroid/os/ParcelFileDescriptor;)V", False), ("(Landroid/content/res/Resources;I)V", False), ("(Landroid/os/ParcelFileDescriptor;JJ)V", False)]
        setSlant = JavaMethod("(I)Landroid/graphics/fonts/Font$Builder;")
        setTtcIndex = JavaMethod("(I)Landroid/graphics/fonts/Font$Builder;")
        setWeight = JavaMethod("(I)Landroid/graphics/fonts/Font$Builder;")
        build = JavaMethod("()Landroid/graphics/fonts/Font;")
        setFontVariationSettings = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/graphics/fonts/Font$Builder;", False, False), ("([Landroid/graphics/fonts/FontVariationAxis;)Landroid/graphics/fonts/Font$Builder;", False, False)])

class FontStyle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/fonts/FontStyle"
    __javaconstructor__ = [("()V", False), ("(II)V", False)]
    FONT_SLANT_ITALIC = JavaStaticField("I")
    FONT_SLANT_UPRIGHT = JavaStaticField("I")
    FONT_WEIGHT_BLACK = JavaStaticField("I")
    FONT_WEIGHT_BOLD = JavaStaticField("I")
    FONT_WEIGHT_EXTRA_BOLD = JavaStaticField("I")
    FONT_WEIGHT_EXTRA_LIGHT = JavaStaticField("I")
    FONT_WEIGHT_LIGHT = JavaStaticField("I")
    FONT_WEIGHT_MAX = JavaStaticField("I")
    FONT_WEIGHT_MEDIUM = JavaStaticField("I")
    FONT_WEIGHT_MIN = JavaStaticField("I")
    FONT_WEIGHT_NORMAL = JavaStaticField("I")
    FONT_WEIGHT_SEMI_BOLD = JavaStaticField("I")
    FONT_WEIGHT_THIN = JavaStaticField("I")
    FONT_WEIGHT_UNSPECIFIED = JavaStaticField("I")
    getSlant = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getWeight = JavaMethod("()I")

class SystemFonts(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/fonts/SystemFonts"
    getAvailableFonts = JavaStaticMethod("()Ljava/util/Set;")

class FontVariationAxis(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/fonts/FontVariationAxis"
    __javaconstructor__ = [("(Ljava/lang/String;F)V", False)]
    fromFontVariationSettings = JavaStaticMethod("(Ljava/lang/String;)[Landroid/graphics/fonts/FontVariationAxis;")
    getStyleValue = JavaMethod("()F")
    toFontVariationSettings = JavaStaticMethod("([Landroid/graphics/fonts/FontVariationAxis;)Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getTag = JavaMethod("()Ljava/lang/String;")