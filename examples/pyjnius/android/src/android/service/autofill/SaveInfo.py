from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SaveInfo"]

class SaveInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/SaveInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_DELAY_SAVE = JavaStaticField("I")
    FLAG_DONT_SAVE_ON_FINISH = JavaStaticField("I")
    FLAG_SAVE_ON_ALL_VIEWS_INVISIBLE = JavaStaticField("I")
    NEGATIVE_BUTTON_STYLE_CANCEL = JavaStaticField("I")
    NEGATIVE_BUTTON_STYLE_NEVER = JavaStaticField("I")
    NEGATIVE_BUTTON_STYLE_REJECT = JavaStaticField("I")
    POSITIVE_BUTTON_STYLE_CONTINUE = JavaStaticField("I")
    POSITIVE_BUTTON_STYLE_SAVE = JavaStaticField("I")
    SAVE_DATA_TYPE_ADDRESS = JavaStaticField("I")
    SAVE_DATA_TYPE_CREDIT_CARD = JavaStaticField("I")
    SAVE_DATA_TYPE_DEBIT_CARD = JavaStaticField("I")
    SAVE_DATA_TYPE_EMAIL_ADDRESS = JavaStaticField("I")
    SAVE_DATA_TYPE_GENERIC = JavaStaticField("I")
    SAVE_DATA_TYPE_GENERIC_CARD = JavaStaticField("I")
    SAVE_DATA_TYPE_PASSWORD = JavaStaticField("I")
    SAVE_DATA_TYPE_PAYMENT_CARD = JavaStaticField("I")
    SAVE_DATA_TYPE_USERNAME = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/SaveInfo$Builder"
        __javaconstructor__ = [("(I)V", False), ("(I[Landroid/view/autofill/AutofillId;)V", False)]
        addSanitizer = JavaMethod("(Landroid/service/autofill/Sanitizer;[Landroid/view/autofill/AutofillId;)Landroid/service/autofill/SaveInfo$Builder;", varargs=True)
        setNegativeAction = JavaMethod("(ILandroid/content/IntentSender;)Landroid/service/autofill/SaveInfo$Builder;")
        setOptionalIds = JavaMethod("([Landroid/view/autofill/AutofillId;)Landroid/service/autofill/SaveInfo$Builder;")
        setPositiveAction = JavaMethod("(I)Landroid/service/autofill/SaveInfo$Builder;")
        setTriggerId = JavaMethod("(Landroid/view/autofill/AutofillId;)Landroid/service/autofill/SaveInfo$Builder;")
        setCustomDescription = JavaMethod("(Landroid/service/autofill/CustomDescription;)Landroid/service/autofill/SaveInfo$Builder;")
        setDescription = JavaMethod("(Ljava/lang/CharSequence;)Landroid/service/autofill/SaveInfo$Builder;")
        setFlags = JavaMethod("(I)Landroid/service/autofill/SaveInfo$Builder;")
        build = JavaMethod("()Landroid/service/autofill/SaveInfo;")
        setValidator = JavaMethod("(Landroid/service/autofill/Validator;)Landroid/service/autofill/SaveInfo$Builder;")