from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ContentCaptureManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/ContentCaptureManager"
    DATA_SHARE_ERROR_CONCURRENT_REQUEST = JavaStaticField("I")
    DATA_SHARE_ERROR_TIMEOUT_INTERRUPTED = JavaStaticField("I")
    DATA_SHARE_ERROR_UNKNOWN = JavaStaticField("I")
    getContentCaptureConditions = JavaMethod("()Ljava/util/Set;")
    getServiceComponentName = JavaMethod("()Landroid/content/ComponentName;")
    isContentCaptureEnabled = JavaMethod("()Z")
    removeData = JavaMethod("(Landroid/view/contentcapture/DataRemovalRequest;)V")
    setContentCaptureEnabled = JavaMethod("(Z)V")
    shareData = JavaMethod("(Landroid/view/contentcapture/DataShareRequest;Ljava/util/concurrent/Executor;Landroid/view/contentcapture/DataShareWriteAdapter;)V")

class ContentCaptureSessionId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/ContentCaptureSessionId"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class ContentCaptureSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/ContentCaptureSession"
    getContentCaptureSessionId = JavaMethod("()Landroid/view/contentcapture/ContentCaptureSessionId;")
    getContentCaptureContext = JavaMethod("()Landroid/view/contentcapture/ContentCaptureContext;")
    createContentCaptureSession = JavaMethod("(Landroid/view/contentcapture/ContentCaptureContext;)Landroid/view/contentcapture/ContentCaptureSession;")
    newAutofillId = JavaMethod("(Landroid/view/autofill/AutofillId;J)Landroid/view/autofill/AutofillId;")
    newViewStructure = JavaMethod("(Landroid/view/View;)Landroid/view/ViewStructure;")
    newVirtualViewStructure = JavaMethod("(Landroid/view/autofill/AutofillId;J)Landroid/view/ViewStructure;")
    notifySessionPaused = JavaMethod("()V")
    notifySessionResumed = JavaMethod("()V")
    notifyViewAppeared = JavaMethod("(Landroid/view/ViewStructure;)V")
    notifyViewDisappeared = JavaMethod("(Landroid/view/autofill/AutofillId;)V")
    notifyViewInsetsChanged = JavaMethod("(Landroid/graphics/Insets;)V")
    notifyViewTextChanged = JavaMethod("(Landroid/view/autofill/AutofillId;Ljava/lang/CharSequence;)V")
    notifyViewsAppeared = JavaMethod("(Ljava/util/List;)V")
    notifyViewsDisappeared = JavaMethod("(Landroid/view/autofill/AutofillId;[J)V")
    setContentCaptureContext = JavaMethod("(Landroid/view/contentcapture/ContentCaptureContext;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    flush = JavaMethod("()V")
    destroy = JavaMethod("()V")
    close = JavaMethod("()V")

class ContentCaptureContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/ContentCaptureContext"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getLocusId = JavaMethod("()Landroid/content/LocusId;")
    forLocusId = JavaStaticMethod("(Ljava/lang/String;)Landroid/view/contentcapture/ContentCaptureContext;")
    toString = JavaMethod("()Ljava/lang/String;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/contentcapture/ContentCaptureContext$Builder"
        __javaconstructor__ = [("(Landroid/content/LocusId;)V", False)]
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/contentcapture/ContentCaptureContext$Builder;")
        build = JavaMethod("()Landroid/view/contentcapture/ContentCaptureContext;")

class DataRemovalRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/DataRemovalRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_IS_PREFIX = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isForEverything = JavaMethod("()Z")
    getLocusIdRequests = JavaMethod("()Ljava/util/List;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class LocusIdRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/contentcapture/DataRemovalRequest$LocusIdRequest"
        getLocusId = JavaMethod("()Landroid/content/LocusId;")
        getFlags = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/contentcapture/DataRemovalRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        addLocusId = JavaMethod("(Landroid/content/LocusId;I)Landroid/view/contentcapture/DataRemovalRequest$Builder;")
        forEverything = JavaMethod("()Landroid/view/contentcapture/DataRemovalRequest$Builder;")
        build = JavaMethod("()Landroid/view/contentcapture/DataRemovalRequest;")

class ContentCaptureCondition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/ContentCaptureCondition"
    __javaconstructor__ = [("(Landroid/content/LocusId;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_IS_REGEX = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getLocusId = JavaMethod("()Landroid/content/LocusId;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getFlags = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class DataShareRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/DataShareRequest"
    __javaconstructor__ = [("(Landroid/content/LocusId;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getMimeType = JavaMethod("()Ljava/lang/String;")
    getLocusId = JavaMethod("()Landroid/content/LocusId;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class DataShareWriteAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/DataShareWriteAdapter"
    onRejected = JavaMethod("()V")
    onError = JavaMethod("(I)V")
    onWrite = JavaMethod("(Landroid/os/ParcelFileDescriptor;)V")