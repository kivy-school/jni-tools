from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClipData"]

class ClipData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ClipData"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;[Ljava/lang/String;Landroid/content/ClipData$Item;)V", False), ("(Landroid/content/ClipDescription;Landroid/content/ClipData$Item;)V", False), ("(Landroid/content/ClipData;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    newPlainText = JavaStaticMethod("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Landroid/content/ClipData;")
    newHtmlText = JavaStaticMethod("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;Ljava/lang/String;)Landroid/content/ClipData;")
    newIntent = JavaStaticMethod("(Ljava/lang/CharSequence;Landroid/content/Intent;)Landroid/content/ClipData;")
    newUri = JavaStaticMethod("(Landroid/content/ContentResolver;Ljava/lang/CharSequence;Landroid/net/Uri;)Landroid/content/ClipData;")
    newRawUri = JavaStaticMethod("(Ljava/lang/CharSequence;Landroid/net/Uri;)Landroid/content/ClipData;")
    getDescription = JavaMethod("()Landroid/content/ClipDescription;")
    addItem = JavaMultipleMethod([("(Landroid/content/ClipData$Item;)V", False, False), ("(Landroid/content/ContentResolver;Landroid/content/ClipData$Item;)V", False, False)])
    getItemCount = JavaMethod("()I")
    getItemAt = JavaMethod("(I)Landroid/content/ClipData$Item;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Item(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/ClipData/Item"
        __javaconstructor__ = [("(Ljava/lang/CharSequence;)V", False), ("(Ljava/lang/CharSequence;Ljava/lang/String;)V", False), ("(Landroid/content/Intent;)V", False), ("(Landroid/net/Uri;)V", False), ("(Ljava/lang/CharSequence;Landroid/content/Intent;Landroid/net/Uri;)V", False), ("(Ljava/lang/CharSequence;Ljava/lang/String;Landroid/content/Intent;Landroid/net/Uri;)V", False)]
        getText = JavaMethod("()Ljava/lang/CharSequence;")
        getHtmlText = JavaMethod("()Ljava/lang/String;")
        getIntent = JavaMethod("()Landroid/content/Intent;")
        getIntentSender = JavaMethod("()Landroid/content/IntentSender;")
        getUri = JavaMethod("()Landroid/net/Uri;")
        getTextLinks = JavaMethod("()Landroid/view/textclassifier/TextLinks;")
        coerceToText = JavaMethod("(Landroid/content/Context;)Ljava/lang/CharSequence;")
        coerceToStyledText = JavaMethod("(Landroid/content/Context;)Ljava/lang/CharSequence;")
        coerceToHtmlText = JavaMethod("(Landroid/content/Context;)Ljava/lang/String;")
        toString = JavaMethod("()Ljava/lang/String;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/content/ClipData/Item/Builder"
            __javaconstructor__ = [("()V", False)]
            setText = JavaMethod("(Ljava/lang/CharSequence;)Landroid/content/ClipData$Item$Builder;")
            setHtmlText = JavaMethod("(Ljava/lang/String;)Landroid/content/ClipData$Item$Builder;")
            setIntent = JavaMethod("(Landroid/content/Intent;)Landroid/content/ClipData$Item$Builder;")
            setIntentSender = JavaMethod("(Landroid/content/IntentSender;)Landroid/content/ClipData$Item$Builder;")
            setUri = JavaMethod("(Landroid/net/Uri;)Landroid/content/ClipData$Item$Builder;")
            build = JavaMethod("()Landroid/content/ClipData$Item;")