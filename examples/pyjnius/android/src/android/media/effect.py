from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class EffectUpdateListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/effect/EffectUpdateListener"
    onEffectUpdated = JavaMethod("(Landroid/media/effect/Effect;Ljava/lang/Object;)V")

class EffectFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/effect/EffectFactory"
    EFFECT_AUTOFIX = JavaStaticField("Ljava/lang/String;")
    EFFECT_BACKDROPPER = JavaStaticField("Ljava/lang/String;")
    EFFECT_BITMAPOVERLAY = JavaStaticField("Ljava/lang/String;")
    EFFECT_BLACKWHITE = JavaStaticField("Ljava/lang/String;")
    EFFECT_BRIGHTNESS = JavaStaticField("Ljava/lang/String;")
    EFFECT_CONTRAST = JavaStaticField("Ljava/lang/String;")
    EFFECT_CROP = JavaStaticField("Ljava/lang/String;")
    EFFECT_CROSSPROCESS = JavaStaticField("Ljava/lang/String;")
    EFFECT_DOCUMENTARY = JavaStaticField("Ljava/lang/String;")
    EFFECT_DUOTONE = JavaStaticField("Ljava/lang/String;")
    EFFECT_FILLLIGHT = JavaStaticField("Ljava/lang/String;")
    EFFECT_FISHEYE = JavaStaticField("Ljava/lang/String;")
    EFFECT_FLIP = JavaStaticField("Ljava/lang/String;")
    EFFECT_GRAIN = JavaStaticField("Ljava/lang/String;")
    EFFECT_GRAYSCALE = JavaStaticField("Ljava/lang/String;")
    EFFECT_LOMOISH = JavaStaticField("Ljava/lang/String;")
    EFFECT_NEGATIVE = JavaStaticField("Ljava/lang/String;")
    EFFECT_POSTERIZE = JavaStaticField("Ljava/lang/String;")
    EFFECT_REDEYE = JavaStaticField("Ljava/lang/String;")
    EFFECT_ROTATE = JavaStaticField("Ljava/lang/String;")
    EFFECT_SATURATE = JavaStaticField("Ljava/lang/String;")
    EFFECT_SEPIA = JavaStaticField("Ljava/lang/String;")
    EFFECT_SHARPEN = JavaStaticField("Ljava/lang/String;")
    EFFECT_STRAIGHTEN = JavaStaticField("Ljava/lang/String;")
    EFFECT_TEMPERATURE = JavaStaticField("Ljava/lang/String;")
    EFFECT_TINT = JavaStaticField("Ljava/lang/String;")
    EFFECT_VIGNETTE = JavaStaticField("Ljava/lang/String;")
    createEffect = JavaMethod("(Ljava/lang/String;)Landroid/media/effect/Effect;")
    isEffectSupported = JavaStaticMethod("(Ljava/lang/String;)Z")

class EffectContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/effect/EffectContext"
    createWithCurrentGlContext = JavaStaticMethod("()Landroid/media/effect/EffectContext;")
    getFactory = JavaMethod("()Landroid/media/effect/EffectFactory;")
    release = JavaMethod("()V")

class Effect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/effect/Effect"
    __javaconstructor__ = [("()V", False)]
    setUpdateListener = JavaMethod("(Landroid/media/effect/EffectUpdateListener;)V")
    setParameter = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    getName = JavaMethod("()Ljava/lang/String;")
    apply = JavaMethod("(IIII)V")
    release = JavaMethod("()V")