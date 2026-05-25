from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SearchableInfo"]

class SearchableInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/SearchableInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getSuggestAuthority = JavaMethod("()Ljava/lang/String;")
    getSuggestPackage = JavaMethod("()Ljava/lang/String;")
    getSearchActivity = JavaMethod("()Landroid/content/ComponentName;")
    shouldRewriteQueryFromData = JavaMethod("()Z")
    shouldRewriteQueryFromText = JavaMethod("()Z")
    getSettingsDescriptionId = JavaMethod("()I")
    getSuggestPath = JavaMethod("()Ljava/lang/String;")
    getSuggestSelection = JavaMethod("()Ljava/lang/String;")
    getSuggestIntentAction = JavaMethod("()Ljava/lang/String;")
    getSuggestIntentData = JavaMethod("()Ljava/lang/String;")
    getSuggestThreshold = JavaMethod("()I")
    getHintId = JavaMethod("()I")
    getVoiceSearchEnabled = JavaMethod("()Z")
    getVoiceSearchLaunchWebSearch = JavaMethod("()Z")
    getVoiceSearchLaunchRecognizer = JavaMethod("()Z")
    getVoiceLanguageModeId = JavaMethod("()I")
    getVoicePromptTextId = JavaMethod("()I")
    getVoiceLanguageId = JavaMethod("()I")
    getVoiceMaxResults = JavaMethod("()I")
    getInputType = JavaMethod("()I")
    getImeOptions = JavaMethod("()I")
    shouldIncludeInGlobalSearch = JavaMethod("()Z")
    queryAfterZeroResults = JavaMethod("()Z")
    autoUrlDetect = JavaMethod("()Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")