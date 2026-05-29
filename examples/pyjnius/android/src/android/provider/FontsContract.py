from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FontsContract"]

class FontsContract(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/FontsContract"
    buildTypeface = JavaStaticMethod("(Landroid/content/Context;Landroid/os/CancellationSignal;[Landroid/provider/FontsContract$FontInfo;)Landroid/graphics/Typeface;")
    fetchFonts = JavaStaticMethod("(Landroid/content/Context;Landroid/os/CancellationSignal;Landroid/provider/FontRequest;)Landroid/provider/FontsContract$FontFamilyResult;")
    requestFonts = JavaStaticMethod("(Landroid/content/Context;Landroid/provider/FontRequest;Landroid/os/Handler;Landroid/os/CancellationSignal;Landroid/provider/FontsContract$FontRequestCallback;)V")

    class FontRequestCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/FontsContract$FontRequestCallback"
        __javaconstructor__ = [("()V", False)]
        FAIL_REASON_FONT_LOAD_ERROR = JavaStaticField("I")
        FAIL_REASON_FONT_NOT_FOUND = JavaStaticField("I")
        FAIL_REASON_FONT_UNAVAILABLE = JavaStaticField("I")
        FAIL_REASON_MALFORMED_QUERY = JavaStaticField("I")
        FAIL_REASON_PROVIDER_NOT_FOUND = JavaStaticField("I")
        FAIL_REASON_WRONG_CERTIFICATES = JavaStaticField("I")
        onTypefaceRequestFailed = JavaMethod("(I)V")
        onTypefaceRetrieved = JavaMethod("(Landroid/graphics/Typeface;)V")

    class FontInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/FontsContract$FontInfo"
        getResultCode = JavaMethod("()I")
        getAxes = JavaMethod("()[Landroid/graphics/fonts/FontVariationAxis;")
        getTtcIndex = JavaMethod("()I")
        getUri = JavaMethod("()Landroid/net/Uri;")
        getWeight = JavaMethod("()I")
        isItalic = JavaMethod("()Z")

    class FontFamilyResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/FontsContract$FontFamilyResult"
        STATUS_OK = JavaStaticField("I")
        STATUS_REJECTED = JavaStaticField("I")
        STATUS_UNEXPECTED_DATA_PROVIDED = JavaStaticField("I")
        STATUS_WRONG_CERTIFICATES = JavaStaticField("I")
        getFonts = JavaMethod("()[Landroid/provider/FontsContract$FontInfo;")
        getStatusCode = JavaMethod("()I")

    class Columns(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/FontsContract$Columns"
        FILE_ID = JavaStaticField("Ljava/lang/String;")
        ITALIC = JavaStaticField("Ljava/lang/String;")
        RESULT_CODE = JavaStaticField("Ljava/lang/String;")
        RESULT_CODE_FONT_NOT_FOUND = JavaStaticField("I")
        RESULT_CODE_FONT_UNAVAILABLE = JavaStaticField("I")
        RESULT_CODE_MALFORMED_QUERY = JavaStaticField("I")
        RESULT_CODE_OK = JavaStaticField("I")
        TTC_INDEX = JavaStaticField("Ljava/lang/String;")
        VARIATION_SETTINGS = JavaStaticField("Ljava/lang/String;")
        WEIGHT = JavaStaticField("Ljava/lang/String;")
        _COUNT = JavaStaticField("Ljava/lang/String;")
        _ID = JavaStaticField("Ljava/lang/String;")