from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Dataset"]

class Dataset(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/Dataset"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/Dataset/Builder"
        __javaconstructor__ = [("(Landroid/widget/RemoteViews;)V", False), ("(Landroid/service/autofill/Presentations;)V", False), ("()V", False)]
        setInlinePresentation = JavaMultipleMethod([("(Landroid/service/autofill/InlinePresentation;)Landroid/service/autofill/Dataset$Builder;", False, False), ("(Landroid/service/autofill/InlinePresentation;Landroid/service/autofill/InlinePresentation;)Landroid/service/autofill/Dataset$Builder;", False, False)])
        setAuthentication = JavaMethod("(Landroid/content/IntentSender;)Landroid/service/autofill/Dataset$Builder;")
        setId = JavaMethod("(Ljava/lang/String;)Landroid/service/autofill/Dataset$Builder;")
        setValue = JavaMultipleMethod([("(Landroid/view/autofill/AutofillId;Landroid/view/autofill/AutofillValue;)Landroid/service/autofill/Dataset$Builder;", False, False), ("(Landroid/view/autofill/AutofillId;Landroid/view/autofill/AutofillValue;Landroid/widget/RemoteViews;)Landroid/service/autofill/Dataset$Builder;", False, False), ("(Landroid/view/autofill/AutofillId;Landroid/view/autofill/AutofillValue;Ljava/util/regex/Pattern;)Landroid/service/autofill/Dataset$Builder;", False, False), ("(Landroid/view/autofill/AutofillId;Landroid/view/autofill/AutofillValue;Ljava/util/regex/Pattern;Landroid/widget/RemoteViews;)Landroid/service/autofill/Dataset$Builder;", False, False), ("(Landroid/view/autofill/AutofillId;Landroid/view/autofill/AutofillValue;Landroid/widget/RemoteViews;Landroid/service/autofill/InlinePresentation;)Landroid/service/autofill/Dataset$Builder;", False, False), ("(Landroid/view/autofill/AutofillId;Landroid/view/autofill/AutofillValue;Landroid/widget/RemoteViews;Landroid/service/autofill/InlinePresentation;Landroid/service/autofill/InlinePresentation;)Landroid/service/autofill/Dataset$Builder;", False, False), ("(Landroid/view/autofill/AutofillId;Landroid/view/autofill/AutofillValue;Ljava/util/regex/Pattern;Landroid/widget/RemoteViews;Landroid/service/autofill/InlinePresentation;)Landroid/service/autofill/Dataset$Builder;", False, False), ("(Landroid/view/autofill/AutofillId;Landroid/view/autofill/AutofillValue;Ljava/util/regex/Pattern;Landroid/widget/RemoteViews;Landroid/service/autofill/InlinePresentation;Landroid/service/autofill/InlinePresentation;)Landroid/service/autofill/Dataset$Builder;", False, False)])
        setField = JavaMultipleMethod([("(Landroid/view/autofill/AutofillId;Landroid/service/autofill/Field;)Landroid/service/autofill/Dataset$Builder;", False, False), ("(Ljava/lang/String;Landroid/service/autofill/Field;)Landroid/service/autofill/Dataset$Builder;", False, False)])
        setFieldForAllHints = JavaMethod("(Landroid/service/autofill/Field;)Landroid/service/autofill/Dataset$Builder;")
        build = JavaMethod("()Landroid/service/autofill/Dataset;")