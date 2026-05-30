from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class RectShape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/shapes/RectShape"
    __javaconstructor__ = [("()V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMultipleMethod([("()Landroid/graphics/drawable/shapes/RectShape;", False, False), ("()Landroid/graphics/drawable/shapes/Shape;", False, False), ("()Ljava/lang/Object;", False, False)])
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")

class OvalShape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/shapes/OvalShape"
    __javaconstructor__ = [("()V", False)]
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/graphics/drawable/shapes/RectShape;", False, False), ("()Landroid/graphics/drawable/shapes/Shape;", False, False), ("()Landroid/graphics/drawable/shapes/OvalShape;", False, False)])
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")

class PathShape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/shapes/PathShape"
    __javaconstructor__ = [("(Landroid/graphics/Path;FF)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/graphics/drawable/shapes/PathShape;", False, False), ("()Landroid/graphics/drawable/shapes/Shape;", False, False)])
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")

class Shape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/shapes/Shape"
    __javaconstructor__ = [("()V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/graphics/drawable/shapes/Shape;", False, False)])
    resize = JavaMethod("(FF)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")
    getHeight = JavaMethod("()F")
    getWidth = JavaMethod("()F")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")
    hasAlpha = JavaMethod("()Z")

class RoundRectShape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/shapes/RoundRectShape"
    __javaconstructor__ = [("([FLandroid/graphics/RectF;[F)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMultipleMethod([("()Landroid/graphics/drawable/shapes/Shape;", False, False), ("()Ljava/lang/Object;", False, False), ("()Landroid/graphics/drawable/shapes/RoundRectShape;", False, False), ("()Landroid/graphics/drawable/shapes/RectShape;", False, False)])
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")

class ArcShape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/shapes/ArcShape"
    __javaconstructor__ = [("(FF)V", False)]
    getSweepAngle = JavaMethod("()F")
    getStartAngle = JavaMethod("()F")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMultipleMethod([("()Landroid/graphics/drawable/shapes/Shape;", False, False), ("()Ljava/lang/Object;", False, False), ("()Landroid/graphics/drawable/shapes/RectShape;", False, False), ("()Landroid/graphics/drawable/shapes/ArcShape;", False, False)])
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")