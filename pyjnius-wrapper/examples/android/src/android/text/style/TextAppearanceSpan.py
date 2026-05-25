from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextAppearanceSpan"]

class TextAppearanceSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/TextAppearanceSpan"
    __javaconstructor__ = [("(Landroid/content/Context;I)V", False), ("(Landroid/content/Context;II)V", False), ("(Ljava/lang/String;IILandroid/content/res/ColorStateList;Landroid/content/res/ColorStateList;)V", False), ("(Landroid/os/Parcel;)V", False)]
    getSpanTypeId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getFamily = JavaMethod("()Ljava/lang/String;")
    getTextColor = JavaMethod("()Landroid/content/res/ColorStateList;")
    getLinkTextColor = JavaMethod("()Landroid/content/res/ColorStateList;")
    getTextSize = JavaMethod("()I")
    getTextStyle = JavaMethod("()I")
    getTextFontWeight = JavaMethod("()I")
    getTextLocales = JavaMethod("()Landroid/os/LocaleList;")
    getTypeface = JavaMethod("()Landroid/graphics/Typeface;")
    getShadowColor = JavaMethod("()I")
    getShadowDx = JavaMethod("()F")
    getShadowDy = JavaMethod("()F")
    getShadowRadius = JavaMethod("()F")
    getFontFeatureSettings = JavaMethod("()Ljava/lang/String;")
    getFontVariationSettings = JavaMethod("()Ljava/lang/String;")
    isElegantTextHeight = JavaMethod("()Z")
    getLetterSpacing = JavaMethod("()F")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    updateMeasureState = JavaMethod("(Landroid/text/TextPaint;)V")
    toString = JavaMethod("()Ljava/lang/String;")