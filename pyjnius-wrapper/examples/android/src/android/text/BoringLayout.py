from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BoringLayout"]

class BoringLayout(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/BoringLayout"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;Landroid/text/TextPaint;ILandroid/text/Layout$Alignment;FFLandroid/text/BoringLayout$Metrics;Z)V", False), ("(Ljava/lang/CharSequence;Landroid/text/TextPaint;ILandroid/text/Layout$Alignment;FFLandroid/text/BoringLayout$Metrics;ZLandroid/text/TextUtils$TruncateAt;I)V", False), ("(Ljava/lang/CharSequence;Landroid/text/TextPaint;ILandroid/text/Layout$Alignment;FFLandroid/text/BoringLayout$Metrics;ZLandroid/text/TextUtils$TruncateAt;IZ)V", False)]
    make = JavaMultipleMethod([("(Ljava/lang/CharSequence;Landroid/text/TextPaint;ILandroid/text/Layout$Alignment;FFLandroid/text/BoringLayout$Metrics;Z)Landroid/text/BoringLayout;", True, False), ("(Ljava/lang/CharSequence;Landroid/text/TextPaint;ILandroid/text/Layout$Alignment;FFLandroid/text/BoringLayout$Metrics;ZLandroid/text/TextUtils$TruncateAt;I)Landroid/text/BoringLayout;", True, False), ("(Ljava/lang/CharSequence;Landroid/text/TextPaint;ILandroid/text/Layout$Alignment;Landroid/text/BoringLayout$Metrics;ZLandroid/text/TextUtils$TruncateAt;IZ)Landroid/text/BoringLayout;", True, False)])
    replaceOrMake = JavaMultipleMethod([("(Ljava/lang/CharSequence;Landroid/text/TextPaint;ILandroid/text/Layout$Alignment;FFLandroid/text/BoringLayout$Metrics;Z)Landroid/text/BoringLayout;", False, False), ("(Ljava/lang/CharSequence;Landroid/text/TextPaint;ILandroid/text/Layout$Alignment;Landroid/text/BoringLayout$Metrics;ZLandroid/text/TextUtils$TruncateAt;IZ)Landroid/text/BoringLayout;", False, False), ("(Ljava/lang/CharSequence;Landroid/text/TextPaint;ILandroid/text/Layout$Alignment;FFLandroid/text/BoringLayout$Metrics;ZLandroid/text/TextUtils$TruncateAt;I)Landroid/text/BoringLayout;", False, False)])
    isBoring = JavaMultipleMethod([("(Ljava/lang/CharSequence;Landroid/text/TextPaint;)Landroid/text/BoringLayout$Metrics;", True, False), ("(Ljava/lang/CharSequence;Landroid/text/TextPaint;Landroid/text/BoringLayout$Metrics;)Landroid/text/BoringLayout$Metrics;", True, False), ("(Ljava/lang/CharSequence;Landroid/text/TextPaint;Landroid/text/TextDirectionHeuristic;ZLandroid/text/BoringLayout$Metrics;)Landroid/text/BoringLayout$Metrics;", True, False)])
    getHeight = JavaMethod("()I")
    getLineCount = JavaMethod("()I")
    getLineTop = JavaMethod("(I)I")
    getLineDescent = JavaMethod("(I)I")
    getLineStart = JavaMethod("(I)I")
    getParagraphDirection = JavaMethod("(I)I")
    getLineContainsTab = JavaMethod("(I)Z")
    getLineMax = JavaMethod("(I)F")
    getLineWidth = JavaMethod("(I)F")
    getLineDirections = JavaMethod("(I)Landroid/text/Layout$Directions;")
    getTopPadding = JavaMethod("()I")
    getBottomPadding = JavaMethod("()I")
    getEllipsisCount = JavaMethod("(I)I")
    getEllipsisStart = JavaMethod("(I)I")
    getEllipsizedWidth = JavaMethod("()I")
    isFallbackLineSpacingEnabled = JavaMethod("()Z")
    computeDrawingBoundingBox = JavaMethod("()Landroid/graphics/RectF;")
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Path;Landroid/graphics/Paint;I)V")
    ellipsized = JavaMethod("(II)V")

    class Metrics(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/BoringLayout/Metrics"
        __javaconstructor__ = [("()V", False)]
        width = JavaField("I")
        getDrawingBoundingBox = JavaMethod("()Landroid/graphics/RectF;")
        toString = JavaMethod("()Ljava/lang/String;")