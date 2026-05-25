from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GestureDescription"]

class GestureDescription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accessibilityservice/GestureDescription"
    getMaxStrokeCount = JavaStaticMethod("()I")
    getMaxGestureDuration = JavaStaticMethod("()J")
    getStrokeCount = JavaMethod("()I")
    getStroke = JavaMethod("(I)Landroid/accessibilityservice/GestureDescription$StrokeDescription;")
    getDisplayId = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/accessibilityservice/GestureDescription/Builder"
        __javaconstructor__ = [("()V", False)]
        addStroke = JavaMethod("(Landroid/accessibilityservice/GestureDescription$StrokeDescription;)Landroid/accessibilityservice/GestureDescription$Builder;")
        setDisplayId = JavaMethod("(I)Landroid/accessibilityservice/GestureDescription$Builder;")
        build = JavaMethod("()Landroid/accessibilityservice/GestureDescription;")

    class StrokeDescription(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/accessibilityservice/GestureDescription/StrokeDescription"
        __javaconstructor__ = [("(Landroid/graphics/Path;JJ)V", False), ("(Landroid/graphics/Path;JJZ)V", False)]
        getPath = JavaMethod("()Landroid/graphics/Path;")
        getStartTime = JavaMethod("()J")
        getDuration = JavaMethod("()J")
        continueStroke = JavaMethod("(Landroid/graphics/Path;JJZ)Landroid/accessibilityservice/GestureDescription$StrokeDescription;")
        willContinue = JavaMethod("()Z")