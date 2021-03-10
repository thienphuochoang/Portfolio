/*
- File structure from 3dsMax's StandardFX11.fx
- PBR Algorithm from UE4
- IBL Diffuse/Specular Cubemaps created by IBL Baker
*/

string ParamID = "0x003";

float Script : STANDARDSGLOBAL <
    string UIWidget = "none";
    string ScriptClass = "object";
    string ScriptOrder = "standard";
    string ScriptOutput = "color";
    string Script = "Technique=Main;";
> = 0.8;

// UV Channel 2 for Occlusion
#define _USE_MAP_2_CHANNEL_

//// UN-TWEAKABLES - AUTOMATICALLY-TRACKED TRANSFORMS ////////////////

float4x4 WorldITXf : WorldInverseTranspose < string UIWidget="None"; >;
float4x4 WvpXf : WorldViewProjection < string UIWidget="None"; >;
float4x4 WorldXf : World < string UIWidget="None"; >;
float4x4 ViewIXf : ViewInverse < string UIWidget="None"; >;

/////////////////// ASSIGN VERTEX'S INFO TO REGISTERS (TEXCOORD0 - TEXCOORDn) ////////////////
int texcoord0 : Texcoord
<
	int Texcoord = 0;  // Register TEXCOORD0
	int MapChannel = 1; // Map Channel 1
	string UIWidget = "None";
>;

#ifdef _USE_MAP_2_CHANNEL_
int texcoord1 : Texcoord
<
	int Texcoord = 1;  // Register TEXCOORD1
	int MapChannel = 2; // Map Channel 2
	string UIWidget = "None";
>;
#endif

///////////////////  TWEAKABLE PARAMETERS - COLORS - TEXTURES ////////////////////

////-------------- 1. Attributes

// ------- Normal Map Controls: BumpScale + FlipGreen
float g_NormalMapBumpScale <
	string UIName = "Normal Map";
	string UIWidget = "slider";
	float UIMin = 0.0f;
	float UIMax = 10.0f;
	float UIStep = 0.01f;
>   = 1.0f;
bool g_NormalMapFlipGreen <
	string UIName = "Normal Map - Flip Green";
> = false;
bool g_NormalMapDisable <
	string UIName = "Normal Map - Disable";
> = false;

// ------- IBL (Env) Controls
float g_IblEnvRotation <
	string UIName = "IBL Env Rotation";
	string UIWidget = "slider";
	float UIMin = 0.0f;
	float UIMax = 360.0f;
	float UIStep = 0.5f;
>   = 0.0f;

// ------- IBL Scale
float g_IblSpecScale <
	string UIName = "IBL Spec Scale";
	string UIWidget = "slider";
	float UIMin = 0.0f;
	float UIMax = 5.0f;
	float UIStep = 0.01f;
>   = 1.0f;
float g_IblDiffScale <
	string UIName = "IBL Diff Scale";
	string UIWidget = "slider";
	float UIMin = 0.0f;
	float UIMax = 5.0f;
	float UIStep = 0.01f;
>   = 1.0f;

// ------- Exposure
float g_SceneExposure <
	string UIName = "Scene Exposure Exponent";
	string UIWidget = "slider";
	float UIMin = 0.0f;
	float UIMax = 10.0f;
	float UIStep = 0.01f;
>   = 0.0f;


// ------- ToneMapping Method
int g_SceneToneMappingMethod <
	string UIName = "Scene ToneMapping";
	string UIWidget = "slider";
	float UIMin = 1;	
	float UIMax = 3;	
>  = 1;


// ------- Debug Mode
int g_SceneDebugMode <
	string UIName = "Scene Debug Mode";
	string UIWidget = "slider";
	float UIMin = 0;	
	float UIMax = 50;	
>  = 0;

// ------- Debug Mode plus: Discard Rendering
bool g_DiscardRendering <
	string UIName = "Discard Rendering";
> = false;

////------------- 2. Textures
// Albedo Map
Texture2D g_AlbedoTexture < 
	string UIName = "Albedo Map";
	string ResourceType = "2D";
>;
// Normal Map
Texture2D g_NormalTexture < 
	string UIName = "Normal Map";
	string ResourceType = "2D";
>;
// Surface Map
Texture2D g_SurfaceTexture < 
	string UIName = "Surface Map";
	string ResourceType = "2D";
>;
// Occlusion Map
Texture2D g_OcclusionTexture < 
	string UIName = "Occlusion Map";
	string ResourceType = "2D";
>;

// IBL Cubemaps
TextureCube g_IblSpecTexture < 
	string UIName = "IBL Spec";
	string ResourceType = "CUBE";
>;

TextureCube g_IblDiffTexture < 
	string UIName = "IBL Diff";
	string ResourceType = "CUBE";
>;

Texture2D g_IblBrdfTexture < 
	string UIName = "IBL Brdf";
	string ResourceType = "2D";
>;

// Checker Texture
Texture2D g_CheckerTexture < 
	string UIName = "Checker Map";
	string ResourceType = "2D";
>;

////------------- SamplerState
// +++ Texture2D  Sampler
SamplerState SamplerAnisoWrap
{
	Filter = ANISOTROPIC;
	AddressU = Wrap;
	AddressV = Wrap;
};

// + CubeMapSampler
SamplerState CubeMapSampler
{
	Filter = ANISOTROPIC;
	AddressU = Clamp;
	AddressV = Clamp;
	AddressW = Clamp;    
};

/////////////////// Part V.     DEFINE STRUCTS FOR VERTEX SHADER AND PIXEL SHADER ////////////////////
/* data from application vertex buffer */
struct appdata {
	float4 Position		: POSITION;
	float3 Normal		: NORMAL;
	float3 Tangent		: TANGENT;
	float3 Binormal		: BINORMAL;

	float2 UV0		: TEXCOORD0;

	#ifdef _USE_MAP_2_CHANNEL_
		float2 UV1		: TEXCOORD1;
	#endif

	// More Channel
	#ifdef _USE_VERT_ALPHA_CHANNEL_
		float3 Alpha		: TEXCOORD2;
	#endif
};

/* data passed from vertex shader to pixel shader */
struct vertexOutput {
    float4 HPosition	: SV_Position;

    float4 UV0		: TEXCOORD0;
	#ifdef _USE_MAP_2_CHANNEL_
		float4 UV1		: TEXCOORD6;
	#endif

    // The following values are passed in "World" coordinates since
    //   it tends to be the most flexible and easy for handling
    //   reflections, sky lighting, and other "global" effects.
    float3 WorldNormal	: TEXCOORD2;
    float3 WorldTangent	: TEXCOORD3;
    float3 WorldBinormal : TEXCOORD4;
    float3 WorldView	: TEXCOORD5;
	
	float4 wPos		: TEXCOORD8;
};



/////////////////// Part VI.     VERTEX SHADING ////////////////////

/*********** Generic Vertex Shader ******/

vertexOutput std_VS(appdata IN) {
    vertexOutput OUT = (vertexOutput)0;
    OUT.WorldNormal = mul(IN.Normal,WorldITXf).xyz;
    OUT.WorldTangent = mul(IN.Tangent,WorldITXf).xyz;
    OUT.WorldBinormal = mul(IN.Binormal,WorldITXf).xyz;
    float4 Po = float4(IN.Position.xyz,1);
    float3 Pw = mul(Po,WorldXf).xyz;
    OUT.WorldView = normalize(ViewIXf[3].xyz - Pw);
    OUT.HPosition = mul(Po,WvpXf);
	OUT.wPos = mul(IN.Position, WorldXf);
	
	OUT.UV0.xy = IN.UV0.xy;

	#ifdef _USE_MAP_2_CHANNEL_
   		OUT.UV1.xy = IN.UV1.xy;
	#endif

    return OUT;
}