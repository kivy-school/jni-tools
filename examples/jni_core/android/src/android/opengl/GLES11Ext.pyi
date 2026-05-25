from typing import Any, ClassVar, overload
from java.nio.Buffer import Buffer
from java.nio.FloatBuffer import FloatBuffer
from java.nio.IntBuffer import IntBuffer
from java.nio.ShortBuffer import ShortBuffer

class GLES11Ext:
    GL_3DC_XY_AMD: ClassVar[int]
    GL_3DC_X_AMD: ClassVar[int]
    GL_ATC_RGBA_EXPLICIT_ALPHA_AMD: ClassVar[int]
    GL_ATC_RGBA_INTERPOLATED_ALPHA_AMD: ClassVar[int]
    GL_ATC_RGB_AMD: ClassVar[int]
    GL_BGRA: ClassVar[int]
    GL_BLEND_DST_ALPHA_OES: ClassVar[int]
    GL_BLEND_DST_RGB_OES: ClassVar[int]
    GL_BLEND_EQUATION_ALPHA_OES: ClassVar[int]
    GL_BLEND_EQUATION_OES: ClassVar[int]
    GL_BLEND_EQUATION_RGB_OES: ClassVar[int]
    GL_BLEND_SRC_ALPHA_OES: ClassVar[int]
    GL_BLEND_SRC_RGB_OES: ClassVar[int]
    GL_BUFFER_ACCESS_OES: ClassVar[int]
    GL_BUFFER_MAPPED_OES: ClassVar[int]
    GL_BUFFER_MAP_POINTER_OES: ClassVar[int]
    GL_COLOR_ATTACHMENT0_OES: ClassVar[int]
    GL_CURRENT_PALETTE_MATRIX_OES: ClassVar[int]
    GL_DECR_WRAP_OES: ClassVar[int]
    GL_DEPTH24_STENCIL8_OES: ClassVar[int]
    GL_DEPTH_ATTACHMENT_OES: ClassVar[int]
    GL_DEPTH_COMPONENT16_OES: ClassVar[int]
    GL_DEPTH_COMPONENT24_OES: ClassVar[int]
    GL_DEPTH_COMPONENT32_OES: ClassVar[int]
    GL_DEPTH_STENCIL_OES: ClassVar[int]
    GL_ETC1_RGB8_OES: ClassVar[int]
    GL_FIXED_OES: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_OES: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_OES: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_OES: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_OES: ClassVar[int]
    GL_FRAMEBUFFER_BINDING_OES: ClassVar[int]
    GL_FRAMEBUFFER_COMPLETE_OES: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_OES: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_OES: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_FORMATS_OES: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_OES: ClassVar[int]
    GL_FRAMEBUFFER_OES: ClassVar[int]
    GL_FRAMEBUFFER_UNSUPPORTED_OES: ClassVar[int]
    GL_FUNC_ADD_OES: ClassVar[int]
    GL_FUNC_REVERSE_SUBTRACT_OES: ClassVar[int]
    GL_FUNC_SUBTRACT_OES: ClassVar[int]
    GL_INCR_WRAP_OES: ClassVar[int]
    GL_INVALID_FRAMEBUFFER_OPERATION_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_BUFFER_BINDING_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_POINTER_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_SIZE_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_STRIDE_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_TYPE_OES: ClassVar[int]
    GL_MATRIX_PALETTE_OES: ClassVar[int]
    GL_MAX_CUBE_MAP_TEXTURE_SIZE_OES: ClassVar[int]
    GL_MAX_PALETTE_MATRICES_OES: ClassVar[int]
    GL_MAX_RENDERBUFFER_SIZE_OES: ClassVar[int]
    GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT: ClassVar[int]
    GL_MAX_VERTEX_UNITS_OES: ClassVar[int]
    GL_MIRRORED_REPEAT_OES: ClassVar[int]
    GL_MODELVIEW_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_NONE_OES: ClassVar[int]
    GL_NORMAL_MAP_OES: ClassVar[int]
    GL_PROJECTION_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_REFLECTION_MAP_OES: ClassVar[int]
    GL_RENDERBUFFER_ALPHA_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_BINDING_OES: ClassVar[int]
    GL_RENDERBUFFER_BLUE_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_DEPTH_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_GREEN_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_HEIGHT_OES: ClassVar[int]
    GL_RENDERBUFFER_INTERNAL_FORMAT_OES: ClassVar[int]
    GL_RENDERBUFFER_OES: ClassVar[int]
    GL_RENDERBUFFER_RED_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_STENCIL_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_WIDTH_OES: ClassVar[int]
    GL_REQUIRED_TEXTURE_IMAGE_UNITS_OES: ClassVar[int]
    GL_RGB565_OES: ClassVar[int]
    GL_RGB5_A1_OES: ClassVar[int]
    GL_RGB8_OES: ClassVar[int]
    GL_RGBA4_OES: ClassVar[int]
    GL_RGBA8_OES: ClassVar[int]
    GL_SAMPLER_EXTERNAL_OES: ClassVar[int]
    GL_STENCIL_ATTACHMENT_OES: ClassVar[int]
    GL_STENCIL_INDEX1_OES: ClassVar[int]
    GL_STENCIL_INDEX4_OES: ClassVar[int]
    GL_STENCIL_INDEX8_OES: ClassVar[int]
    GL_TEXTURE_BINDING_CUBE_MAP_OES: ClassVar[int]
    GL_TEXTURE_BINDING_EXTERNAL_OES: ClassVar[int]
    GL_TEXTURE_CROP_RECT_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_X_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_X_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_Y_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_Z_OES: ClassVar[int]
    GL_TEXTURE_EXTERNAL_OES: ClassVar[int]
    GL_TEXTURE_GEN_MODE_OES: ClassVar[int]
    GL_TEXTURE_GEN_STR_OES: ClassVar[int]
    GL_TEXTURE_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_TEXTURE_MAX_ANISOTROPY_EXT: ClassVar[int]
    GL_UNSIGNED_INT_24_8_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_BUFFER_BINDING_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_POINTER_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_SIZE_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_STRIDE_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_TYPE_OES: ClassVar[int]
    GL_WRITE_ONLY_OES: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def glBlendEquationSeparateOES(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBlendFuncSeparateOES(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glBlendEquationOES(p0: int) -> None: ...
    @staticmethod
    def glDrawTexsOES(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glDrawTexiOES(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glDrawTexxOES(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glDrawTexsvOES(p0: ShortBuffer) -> None: ...
    @overload
    @staticmethod
    def glDrawTexsvOES(p0: Any, p1: int) -> None: ...
    @overload
    @staticmethod
    def glDrawTexivOES(p0: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDrawTexivOES(p0: Any, p1: int) -> None: ...
    @overload
    @staticmethod
    def glDrawTexxvOES(p0: Any, p1: int) -> None: ...
    @overload
    @staticmethod
    def glDrawTexxvOES(p0: IntBuffer) -> None: ...
    @staticmethod
    def glDrawTexfOES(p0: float, p1: float, p2: float, p3: float, p4: float) -> None: ...
    @overload
    @staticmethod
    def glDrawTexfvOES(p0: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glDrawTexfvOES(p0: Any, p1: int) -> None: ...
    @staticmethod
    def glEGLImageTargetTexture2DOES(p0: int, p1: Buffer) -> None: ...
    @staticmethod
    def glEGLImageTargetRenderbufferStorageOES(p0: int, p1: Buffer) -> None: ...
    @staticmethod
    def glAlphaFuncxOES(p0: int, p1: int) -> None: ...
    @staticmethod
    def glClearColorxOES(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glClearDepthxOES(p0: int) -> None: ...
    @overload
    @staticmethod
    def glClipPlanexOES(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glClipPlanexOES(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glColor4xOES(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glDepthRangexOES(p0: int, p1: int) -> None: ...
    @staticmethod
    def glFogxOES(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glFogxvOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glFogxvOES(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glFrustumxOES(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanexOES(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanexOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetFixedvOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetFixedvOES(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetLightxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetLightxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetMaterialxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetMaterialxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnvxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnvxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glLightModelxOES(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glLightModelxvOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glLightModelxvOES(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glLightxOES(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glLightxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glLightxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glLineWidthxOES(p0: int) -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixxOES(p0: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixxOES(p0: Any, p1: int) -> None: ...
    @staticmethod
    def glMaterialxOES(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glMaterialxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glMaterialxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixxOES(p0: Any, p1: int) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixxOES(p0: IntBuffer) -> None: ...
    @staticmethod
    def glMultiTexCoord4xOES(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glNormal3xOES(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glOrthoxOES(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @staticmethod
    def glPointParameterxOES(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glPointParameterxvOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glPointParameterxvOES(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glPointSizexOES(p0: int) -> None: ...
    @staticmethod
    def glPolygonOffsetxOES(p0: int, p1: int) -> None: ...
    @staticmethod
    def glRotatexOES(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glSampleCoveragexOES(p0: int, p1: bool) -> None: ...
    @staticmethod
    def glScalexOES(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glTexEnvxOES(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnvxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnvxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glTexParameterxOES(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glTranslatexOES(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glIsRenderbufferOES(p0: int) -> bool: ...
    @staticmethod
    def glBindRenderbufferOES(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glGenRenderbuffersOES(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenRenderbuffersOES(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glRenderbufferStorageOES(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetRenderbufferParameterivOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetRenderbufferParameterivOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glIsFramebufferOES(p0: int) -> bool: ...
    @staticmethod
    def glBindFramebufferOES(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteFramebuffersOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteFramebuffersOES(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenFramebuffersOES(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenFramebuffersOES(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glCheckFramebufferStatusOES(p0: int) -> int: ...
    @staticmethod
    def glFramebufferRenderbufferOES(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glFramebufferTexture2DOES(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glGetFramebufferAttachmentParameterivOES(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glGetFramebufferAttachmentParameterivOES(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @staticmethod
    def glGenerateMipmapOES(p0: int) -> None: ...
    @staticmethod
    def glCurrentPaletteMatrixOES(p0: int) -> None: ...
    @staticmethod
    def glLoadPaletteFromModelViewMatrixOES() -> None: ...
    @staticmethod
    def glMatrixIndexPointerOES(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @staticmethod
    def glWeightPointerOES(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @staticmethod
    def glDepthRangefOES(p0: float, p1: float) -> None: ...
    @staticmethod
    def glFrustumfOES(p0: float, p1: float, p2: float, p3: float, p4: float, p5: float) -> None: ...
    @staticmethod
    def glOrthofOES(p0: float, p1: float, p2: float, p3: float, p4: float, p5: float) -> None: ...
    @overload
    @staticmethod
    def glClipPlanefOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glClipPlanefOES(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanefOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanefOES(p0: int, p1: FloatBuffer) -> None: ...
    @staticmethod
    def glClearDepthfOES(p0: float) -> None: ...
    @staticmethod
    def glTexGenfOES(p0: int, p1: int, p2: float) -> None: ...
    @overload
    @staticmethod
    def glTexGenfvOES(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexGenfvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glTexGeniOES(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glTexGenivOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexGenivOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glTexGenxOES(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glTexGenxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexGenxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenfvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenfvOES(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenivOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenivOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteRenderbuffersOES(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteRenderbuffersOES(p0: int, p1: Any, p2: int) -> None: ...
