###########################################################
## csapi Class
###########################################################

package ChangeSynergy::csapi;

$VERSION = "1.0";

use strict;
use warnings;
use ChangeSynergy::apiObjectData;
use ChangeSynergy::apiObjectVector;
use ChangeSynergy::apiQueryData;
use ChangeSynergy::apiListObject;
use ChangeSynergy::apiUser;
use ChangeSynergy::apiData;
use ChangeSynergy::util;
use ChangeSynergy::Globals;
use LWP::UserAgent;

sub new
{
	# Initialize data as an empty hash
	my $self = {};

	$self->{globals} = new ChangeSynergy::Globals();

	bless $self;

	return $self;
}

###########################################################
## User Preference Methods
###########################################################
sub GetUserPreference
{
	my $self		= shift;
	my $aUser		= shift;
	my $userName    = shift;
	my $prefName    = shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(ChangeSynergy::util::getUserPreference($aUser, "getUserPreference", $userName, $prefName));
}

sub DumpAUsersPreferences
{
	my $self		= shift;
	my $aUser		= shift;
	my $username	= shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}
	
	return(ChangeSynergy::util::modifyUserPreferences($aUser,$username,"",$self->{globals}->{DUMPPROFILE},"","","",""));
}

sub AddAPreferenceForAllUsers
{
	my $self		= shift;
	my $aUser		= shift;
	my $keyname		= shift;
	my $keyvalue	= shift;
	my $allDBs      = shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}
	
	return(ChangeSynergy::util::modifyUserPreferences($aUser,"",$allDBs,$self->{globals}->{ADD},$keyname,$keyvalue,"",""));
}

sub AddAPreferenceForAUser
{
	my $self		= shift;
	my $aUser		= shift;
	my $username    = shift;
	my $keyname		= shift;
	my $keyvalue	= shift;
	my $allDBs      = shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}
	
	return(ChangeSynergy::util::modifyUserPreferences($aUser,$username,$allDBs,$self->{globals}->{ADD},$keyname,$keyvalue,"",""));
}

sub DeleteAllUserPreferences
{
	my $self		= shift;
	my $aUser		= shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}
	
	return(ChangeSynergy::util::modifyUserPreferences($aUser,"","",$self->{globals}->{DELETE},"","","",""));
}

sub DeleteAUsersPreferences
{
	my $self		= shift;
	my $aUser		= shift;
	my $username    = shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}
	
	return(ChangeSynergy::util::modifyUserPreferences($aUser,$username,"",$self->{globals}->{DELETE},"","","",""));
}

sub DeleteAPreferenceForAllUsers
{
	my $self		= shift;
	my $aUser		= shift;
	my $keyname		= shift;
	my $allDBs      = shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}
	
	return(ChangeSynergy::util::modifyUserPreferences($aUser,"",$allDBs,$self->{globals}->{DELETE},$keyname,"","",""));	
}

sub DeleteAPreferenceForAUser
{
	my $self		= shift;
	my $aUser		= shift;
	my $username    = shift;
	my $keyname		= shift;
	my $allDBs      = shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}
	
	return(ChangeSynergy::util::modifyUserPreferences($aUser,$username,$allDBs,$self->{globals}->{DELETE},$keyname,"","",""));	
}

sub PreferenceNameSubstitutionForAUser
{
	my $self		    = shift;
	my $aUser		    = shift;
	my $username        = shift;
	my $searchValue	    = shift;
	my $replacmentValue = shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}
	
	return(ChangeSynergy::util::modifyUserPreferences($aUser,$username,"",$self->{globals}->{EDIT},"substitute",$searchValue,$self->{globals}->{NAMESUBSTITUTION},$replacmentValue));	
}

sub PreferenceNameSubstitutionForAllUsers
{
	my $self		    = shift;
	my $aUser		    = shift;
	my $searchValue	    = shift;
	my $replacmentValue = shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}
	
	return(ChangeSynergy::util::modifyUserPreferences($aUser,"","",$self->{globals}->{EDIT},"substitute",$searchValue, $self->{globals}->{NAMESUBSTITUTION},$replacmentValue));	
}

sub ChangePreferenceNameForAUser
{
	my $self		= shift;
	my $aUser		= shift;
	my $username    = shift;
	my $keyname		= shift;
	my $keyvalue    = shift;
	my $allDBs      = shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}
	
	return(ChangeSynergy::util::modifyUserPreferences($aUser,$username,$allDBs,$self->{globals}->{EDIT},$keyname,$keyvalue,$self->{globals}->{NAMECHANGE},""));	
}

sub ChangePreferenceNameForAllUsers
{
	my $self		= shift;
	my $aUser		= shift;
	my $keyname		= shift;
	my $keyvalue    = shift;
	my $allDBs      = shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}
	
	return(ChangeSynergy::util::modifyUserPreferences($aUser,"",$allDBs,$self->{globals}->{EDIT},$keyname,$keyvalue,$self->{globals}->{NAMECHANGE},""));	
}

sub PreferenceSubstitutionForAUser
{
	my $self		= shift;
	my $aUser		= shift;
	my $username    = shift;
	my $keyname		= shift;
	my $keyvalue    = shift;
	my $subValue	= shift;
	my $allDBs      = shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}
	
	return(ChangeSynergy::util::modifyUserPreferences($aUser,$username,$allDBs,$self->{globals}->{EDIT},$keyname,$keyvalue,$self->{globals}->{SUBSTITUTION},$subValue));	
}

sub PreferenceSubstitutionForAllUsers
{
	my $self		= shift;
	my $aUser		= shift;
	my $keyname		= shift;
	my $keyvalue    = shift;
	my $subValue	= shift;
	my $allDBs      = shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}
	
	return(ChangeSynergy::util::modifyUserPreferences($aUser,"",$allDBs,$self->{globals}->{EDIT},$keyname,$keyvalue,$self->{globals}->{SUBSTITUTION},$subValue));	
}

sub RefreshUsers
{
	my $self      = shift;
	my $aUser     = shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return ChangeSynergy::util::RefreshUsers($aUser);
}

sub CreateObjectAttributes
{
	my $self      = shift;
	my $aUser     = shift;
	my $cvidList  = shift;
	my $attrData  = shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(ChangeSynergy::util::ModifyObjectsAction($aUser, $cvidList, $attrData, $self->{globals}->{CSAPI_CV_ATTR_CREATE}));
}

sub ModifyObjectAttributes
{
	my $self      = shift;
	my $aUser     = shift;
	my $cvidList  = shift;
	my $attrData  = shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(ChangeSynergy::util::ModifyObjectsAction($aUser, $cvidList, $attrData, $self->{globals}->{CSAPI_CV_ATTR_MODIFY}));
}

sub DeleteObjectAttributes
{
	my $self      = shift;
	my $aUser     = shift;
	my $cvidList  = shift;
	my $attrData  = shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(ChangeSynergy::util::ModifyObjectsAction($aUser, $cvidList, $attrData, $self->{globals}->{CSAPI_CV_ATTR_DELETE}));
}

sub GetObjectData
{
	my $self          = shift;
	my $aUser         = shift;
	my $cvid          = shift;
	my $attributeList = shift;
	my $xmlData       = "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>PreObjectModify</csapi_action_flag>";

	$xmlData .= "<csapi_token>"		. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"		. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"	. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		. $aUser->getUserName()		. "</csapi_user>";

	$xmlData .= "<csapi_attribute_flag>". $attributeList        . "</csapi_attribute_flag>";
	$xmlData .= "<csapi_cvid>"          . $cvid                 . "</csapi_cvid>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub CreateDefaultCSObject
{
	my $self  = shift;
	my $aUser = shift;
	my $name  = shift;

	return(ChangeSynergy::util::NewCVOperation($aUser, "", "", $name, "", "", "TRUE"));
}

sub CreateCSObject
{
	my $self   = shift;
	my $aUser  = shift;
	my $cvtype = shift;
	my $name   = shift;
	my $state  = shift;

	return(ChangeSynergy::util::NewCVOperation($aUser, "", $cvtype, $name, "", $state, "TRUE"));
}

sub CreateNewCV
{
	my $self    = shift;
	my $aUser   = shift;
	my $subsys  = shift;
	my $cvtype  = shift;
	my $name    = shift;
	my $version = shift;
	my $state   = shift;

	return(ChangeSynergy::util::NewCVOperation($aUser, $subsys, $cvtype, $name, $version, $state, "TRUE"));
}

sub DeleteNewCV
{
	my $self    = shift;
	my $aUser   = shift;
	my $subsys  = shift;
	my $cvtype  = shift;
	my $name    = shift;
	my $version = shift;

	return(ChangeSynergy::util::NewCVOperation($aUser, $subsys, $cvtype, $name, $version, "", "FALSE"));
}

sub GetNewCV
{
	my $self    = shift;
	my $aUser   = shift;
	my $subsys  = shift;
	my $cvtype  = shift;
	my $name    = shift;
	my $version = shift;
	my $xmlData = "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>get_new_cv</csapi_action_flag>";

	$xmlData .= "<csapi_token>"		. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"		. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_password>"  . $aUser->getUserPassword() . "</csapi_password>";
	$xmlData .= "<csapi_database>"	. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		. $aUser->getUserName()		. "</csapi_user>";

	$xmlData .= "<csapi_cv_subsys>"  . $subsys  . "</csapi_cv_subsys>";
	$xmlData .= "<csapi_cv_type>"    . $cvtype  . "</csapi_cv_type>";
	$xmlData .= "<csapi_cv_name>"    . $name    . "</csapi_cv_name>";
	$xmlData .= "<csapi_cv_version>" . $version . "</csapi_cv_version>";

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub DeleteCV
{
	my $self    = shift;
	my $aUser   = shift;
	my $cvid    = shift;
	my $xmlData = "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>delete_cv</csapi_action_flag>";

	$xmlData .= "<csapi_token>"		. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"		. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_password>"  . $aUser->getUserPassword() . "</csapi_password>";
	$xmlData .= "<csapi_database>"	. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		. $aUser->getUserName()		. "</csapi_user>";

	$xmlData .= "<csapi_cvid>"      . $cvid                     . "</csapi_cvid>";

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub GetCV
{
	my $self    = shift;
	my $aUser   = shift;
	my $cvid    = shift;
	my $xmlData = "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>get_cv</csapi_action_flag>";

	$xmlData .= "<csapi_token>"		. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"		. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_password>"  . $aUser->getUserPassword() . "</csapi_password>";
	$xmlData .= "<csapi_database>"	. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		. $aUser->getUserName()		. "</csapi_user>";

	$xmlData .= "<csapi_cvid>"      . $cvid                     . "</csapi_cvid>";

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub GetAttributes
{
	my $self    = shift;
	my $aUser   = shift;
	my $xmlData = "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>GetAttributes</csapi_action_flag>";

	$xmlData .= "<csapi_token>"		. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"		. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"	. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		. $aUser->getUserName()		. "</csapi_user>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub SetAttributes
{
	my $self     = shift;
	my $aUser    = shift;
	my $cfgName  = shift;
	my $attrData = shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	if(!defined($attrData))
	{
		die "Data information object is undef";
	}

	my $xmlData = "";
	my $tmp     = $attrData->toAttributeXml();

	$xmlData .= "<csapi_action_flag>SetAttributes</csapi_action_flag>";

	$xmlData .= "<csapi_token>"		. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"		. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"	. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		. $aUser->getUserName()		. "</csapi_user>";

	$xmlData .= "<csapi_cfg_name>"  . $cfgName                  . "</csapi_cfg_name>";
	$xmlData .= $tmp;

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}


###########################################################
## Administrative Methods
###########################################################

sub CreateAttachmentObject
{
	my $self			= shift;
	my $aUser			= shift;
	my $problemNumber	= shift;
	my $relation		= shift;
	my $attachmentName	= shift;
	my $webType			= shift;
	my $comment			= shift;
	my $type			= shift;
	my $isBinary		= shift;
	my $buffer			= shift;
	my $size			= shift;

	return(ChangeSynergy::util::CreateAttachmentObjectBase($aUser, $problemNumber, $relation, $attachmentName,
														   $webType, $comment, $type, $isBinary, $buffer, $size));
}

sub DatabaseGetObject
{
	my $self		= shift;
	my $aUser		= shift;
	my $cvid		= shift;

	return(ChangeSynergy::util::DatabaseGetObjectBase($aUser, $cvid)); 
}

sub DatabaseSetObject
{
	my $self		= shift;
	my $aUser		= shift;	
	my $cvid		= shift;
	my $comment		= shift;
	my $buffer		= shift;
	my $size		= shift;

	return(ChangeSynergy::util::DatabaseSetObjectBase($aUser, $cvid, $comment, $buffer, $size));
}

sub ServerGetFile
{
	my $self	= shift;
	my $aUser	= shift;
	my $file	= shift;

	return(ChangeSynergy::util::ServerGetFileBase($aUser, $file));
}

sub ServerSendFile
{
	my $self	= shift;
	my $aUser	= shift;
	my $buffer	= shift;
	my $size	= shift;

	return(ChangeSynergy::util::ServerSendFileBase($aUser, $buffer, $size));
}

sub ValidateLicense
{
	my $self		= shift;
	my $aUser		= shift;
	my $licenseStr  = shift;
	my $xmlData		= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>ValidateLicense</csapi_action_flag>";
	$xmlData .= "<csapi_token>"		. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"		. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"	. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_action_item>". $licenseStr				. "</csapi_action_item>";

	my $responseData = ChangeSynergy::util::callCsapi($aUser, $xmlData);

	return ($responseData);
}

sub LoadConfigurationData
{
	my $self		= shift;
	my $aUser		= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "loadconfig"));
}

sub LoadAllConfigurationFiles
{
	my $self          = shift;
	my $aUser         = shift;

	return(ChangeSynergy::util::ConfigAdminAction($aUser, "section_loadconfig", "false", "false", "true", "false", "false", "false", "false", "false", "false", "false", "false", "false", ""));
}

sub LoadMergeConfigurationFiles
{
	my $self          = shift;
	my $aUser         = shift;

	return(ChangeSynergy::util::ConfigAdminAction($aUser, "section_loadconfig", "false", "false", "false", "true", "false", "false", "false", "false", "false", "false", "false", "false", ""));
}

sub LoadConfigurationFile
{
	my $self          = shift;
	my $aUser         = shift;
	my $actConfigFile = shift;

	return(ChangeSynergy::util::ConfigAdminAction($aUser, "section_loadconfig", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "true", $actConfigFile));
}

sub BalanceTransactionServer
{
	my $self          = shift;
	my $aUser         = shift;

	return(ChangeSynergy::util::ConfigAdminAction($aUser, "section_loadconfig", "true", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", ""));
}

sub LoadDatabaseListboxes
{
	my $self          = shift;
	my $aUser         = shift;

	return(ChangeSynergy::util::ConfigAdminAction($aUser, "section_loadconfig", "false", "true", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", ""));
}

sub ReloadListboxes
{
	my $self          = shift;
	my $aUser         = shift;

	return(ChangeSynergy::util::ConfigAdminAction($aUser, "section_loadconfig", "false", "true", "false", "false", "false", "false", "false", "false", "false", "false", "false", "true", "pt_listbox.cfg"));
}

sub ClearBusySessions
{
	my $self          = shift;
	my $aUser         = shift;

	return(ChangeSynergy::util::ConfigAdminAction($aUser, "section_loadconfig", "false", "false", "false", "false", "true", "false", "false", "false", "false", "false", "false", "false", ""));
}

sub ResetAdminTokens
{
	my $self          = shift;
	my $aUser         = shift;

	return(ChangeSynergy::util::ConfigAdminAction($aUser, "section_loadconfig", "false", "false", "false", "false", "false", "true", "false", "false", "false", "false", "false", "false", ""));
}

sub ClearAllUserConfigurationData
{
	my $self          = shift;
	my $aUser         = shift;

	return(ChangeSynergy::util::ConfigAdminAction($aUser, "section_loadconfig", "false", "false", "false", "false", "false", "false", "true", "false", "false", "false", "false", "false", ""));
}

sub ClearTransitionUserList
{
	my $self          = shift;
	my $aUser         = shift;

	return(ChangeSynergy::util::ConfigAdminAction($aUser, "section_loadconfig", "false", "false", "false", "false", "false", "false", "false", "true", "false", "false", "false", "false", ""));
}

sub ResetConfigurationDataLoadTime
{
	my $self          = shift;
	my $aUser         = shift;

	return(ChangeSynergy::util::ConfigAdminAction($aUser, "section_loadconfig", "false", "false", "false", "false", "false", "false", "false", "false", "true", "false", "false", "false", ""));
}

sub ResetLDAPPool
{
	my $self          = shift;
	my $aUser         = shift;

	return(ChangeSynergy::util::ConfigAdminAction($aUser, "section_loadconfig", "false", "false", "false", "false", "false", "false", "false", "false", "false", "true", "false", "false", ""));
}

sub ReloadStringTable
{
	my $self          = shift;
	my $aUser         = shift;

	return(ChangeSynergy::util::ConfigAdminAction($aUser, "section_loadconfig", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "true", "false", ""));
}

sub CSHostName
{
	my $self		= shift;
	my $aUser		= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "cs_host_name"));
}

sub CreateUserSecurityData
{
	my $self        = shift;
	my $aUser		= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "set_user_config"));
}

sub ProcessEmailSubmitForms
{
	my $self		= shift;
	my $aUser		= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "process_email_submissions"));
}

sub ToggleDebug
{
	my $self		= shift;
	my $aUser		= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "toggledebug"));
}

sub ClearLog
{
	my $self		= shift;
	my $aUser		= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "clearlog"));
}

sub CreateIndex
{
	my $self		= shift;
	my $aUser		= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "create_index"));
}

sub UpdateIndex
{
	my $self		= shift;
	my $aUser		= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "update_index"));
}

sub EnableIndexing
{
	my $self		= shift;
	my $aUser		= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "enable_indexing"));
}

sub DisableIndexing
{
	my $self		= shift;
	my $aUser		= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "disable_indexing"));
}

sub StopServerAccess
{
	my $self		= shift;
	my $aUser		= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "disable_server"));
}

sub StartServerAccess
{
	my $self		= shift;
	my $aUser		= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "enable_server"));
}

sub ServerAPIVersion
{
	my $self		= shift;
	my $aUser		= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "APIVersion"));
}

sub ClientAPIVersion
{
	my $self		= shift;
	my $aUser		= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(new ChangeSynergy::apiData("4.4"));
}

sub GetHosts
{
	my $self		= shift;
	my $aUser		= shift;

	my $xmlData		= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>server_hosts</csapi_action_flag>";
	$xmlData .= "<csapi_encoded_password>false</csapi_encoded_password>";

	$xmlData .= "<csapi_token>"		. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"		. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_password>"	. $aUser->getUserPassword() . "</csapi_password>";
	$xmlData .= "<csapi_database>"	. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		. $aUser->getUserName()		. "</csapi_user>";

	return(new ChangeSynergy::apiListObject(ChangeSynergy::util::callCsapi($aUser, $xmlData), $self->{globals}->{VALUELISTBOX_TYPE}));
}

sub EnableHost
{
	my $self		= shift;
	my $aUser		= shift;
	my $host		= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "enable_host", $host));
}

sub DisableHost
{
	my $self		= shift;
	my $aUser		= shift;
	my $host		= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "disable_host", $host));
}

sub GetDatabases
{
	my $self		= shift;
	my $aUser		= shift;

	my $xmlData		= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>server_databases</csapi_action_flag>";
	$xmlData .= "<csapi_encoded_password>false</csapi_encoded_password>";

	$xmlData .= "<csapi_token>"		. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"		. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_password>"	. $aUser->getUserPassword() . "</csapi_password>";
	$xmlData .= "<csapi_database>"	. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		. $aUser->getUserName()		. "</csapi_user>";

	return(new ChangeSynergy::apiListObject(ChangeSynergy::util::callCsapi($aUser, $xmlData), $self->{globals}->{VALUELISTBOX_TYPE}));
}

sub EnableDatabase
{
	my $self		= shift;
	my $aUser		= shift;
	my $database	= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "enable_database", $database));
}

sub DisableDatabase
{
	my $self		= shift;
	my $aUser		= shift;
	my $database	= shift;

	return(ChangeSynergy::util::AdminAction($aUser, "disable_database", $database));
}

sub ImportUsersFromAllDatabases
{
	my $self		    = shift;
	my $aUser		    = shift;
	my $overwrite       = shift;
	my $importPassword  = shift;
	my $importEmail     = shift; 
	my $importFirstname = shift;
	my $importLastname  = shift;
	
	
	return(ChangeSynergy::util::importUsers($aUser, "DATABASE", $overwrite, "", "", "",
	       $importPassword, $importEmail, $importFirstname, $importLastname));
}

sub ImportUsersFromCSLDAPServer
{
	my $self	    = shift;
	my $aUser	    = shift;
	my $overwrite       = shift;
	my $importURL       = shift;
	my $importEmail     = shift; 
	my $importFirstname = shift;
	my $importLastname  = shift;
	
	return(ChangeSynergy::util::importUsers($aUser, "LDAP", $overwrite, $importURL, "", "",
	       "", $importEmail, $importFirstname, $importLastname));
}

sub ImportUsersFromAFile
{
	my $self	    = shift;
	my $aUser	    = shift;
	my $overwrite       = shift;
	my $importFile      = shift;
	my $importDelimiter = shift;
	my $importPassword  = shift;
	my $importEmail     = shift; 
	my $importFirstname = shift;
	my $importLastname  = shift;

	my $buf    = "";
	my $buffer = "";
		
	open(INPUTFILE, $importFile) or die "Could not open up the file";

	while($buf = readline *INPUTFILE)
	{
		$buffer .= $buf;
	}

	close(INPUTFILE);
		
	my $size = -s $importFile;

	my $filehandle = ServerSendFile($self, $aUser, $buffer, $size)->getResponseData();
	
	return(ChangeSynergy::util::importUsers($aUser, "FILE", $overwrite, "", $filehandle, $importDelimiter,
	      $importPassword, $importEmail, $importFirstname, $importLastname));
	
}

sub InstallAPackage
{
	my $self        = shift;
	my $aUser	= shift;
	my $packageName = shift;
	
	return(ChangeSynergy::util::packageInstall($aUser, $packageName));

}


###########################################################
## List Object Methods
###########################################################

sub GetValueListBox
{
	my $self		= shift;
	my $aUser		= shift;
	my $listObject  = undef;
	my $configType  = undef;

	if(@_ == 1)
	{
		$listObject  = shift;
		$configType  = $self->{globals}->{SYSTEM_CONFIG};
	}
	elsif(@_ == 2)
	{
		$listObject  = shift;
		$configType  = shift;	
	}

	my $xmlData		= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>GetValueListbox</csapi_action_flag>";
	$xmlData .= "<csapi_encoded_password>false</csapi_encoded_password>";

	$xmlData .= "<csapi_token>"		   . $aUser->getUserToken()    . "</csapi_token>";
	$xmlData .= "<csapi_role>"		   . $aUser->getUserRole()     . "</csapi_role>";
	$xmlData .= "<csapi_password>"	   . $aUser->getUserPassword() . "</csapi_password>";
	$xmlData .= "<csapi_database>"	   . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		   . $aUser->getUserName()     . "</csapi_user>";
	$xmlData .= "<csapi_profile_type>" . $configType               . "</csapi_profile_type>";
	
	$xmlData .= "<csapi_valuelistbox>" . $listObject . "</csapi_valuelistbox>";

	return(new ChangeSynergy::apiListObject(ChangeSynergy::util::callCsapi($aUser, $xmlData), $self->{globals}->{VALUELISTBOX_TYPE}));
}

sub GetListBox
{
	my $self		= shift;
	my $aUser		= shift;
	my $listObject  = undef;
	my $configType  = undef;
	
	if(@_ == 1)
	{
		$listObject  = shift;
		$configType  = $self->{globals}->{SYSTEM_CONFIG};
	}
	elsif(@_ == 2)
	{
		$listObject  = shift;
		$configType  = shift;	
	}

	my $xmlData		= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>GetListbox</csapi_action_flag>";
	$xmlData .= "<csapi_encoded_password>false</csapi_encoded_password>";

	$xmlData .= "<csapi_token>"		   . $aUser->getUserToken()    . "</csapi_token>";
	$xmlData .= "<csapi_role>"		   . $aUser->getUserRole()     . "</csapi_role>";
	$xmlData .= "<csapi_password>"	   . $aUser->getUserPassword() . "</csapi_password>";
	$xmlData .= "<csapi_database>"	   . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		   . $aUser->getUserName()     . "</csapi_user>";
	$xmlData .= "<csapi_profile_type>" . $configType               . "</csapi_profile_type>";
		
	$xmlData .= "<csapi_listbox>" . $listObject . "</csapi_listbox>";

	return(new ChangeSynergy::apiListObject(ChangeSynergy::util::callCsapi($aUser, $xmlData), $self->{globals}->{LISTBOX_TYPE}));
}

sub GetList
{
	my $self		= shift;
	my $aUser		= shift;
	my $listObject  = undef;
	my $configType  = undef;
	
	if(@_ == 1)
	{
		$listObject  = shift;
		$configType  = $self->{globals}->{SYSTEM_CONFIG};
	}
	elsif(@_ == 2)
	{
		$listObject  = shift;
		$configType  = shift;	
	}
	
	my $xmlData		= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>GetList</csapi_action_flag>";
	$xmlData .= "<csapi_encoded_password>false</csapi_encoded_password>";

	$xmlData .= "<csapi_token>"		   . $aUser->getUserToken()    . "</csapi_token>";
	$xmlData .= "<csapi_role>"		   . $aUser->getUserRole()     . "</csapi_role>";
	$xmlData .= "<csapi_password>"	   . $aUser->getUserPassword() . "</csapi_password>";
	$xmlData .= "<csapi_database>"	   . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		   . $aUser->getUserName()     . "</csapi_user>";
	$xmlData .= "<csapi_profile_type>" . $configType               . "</csapi_profile_type>";

	$xmlData .= "<csapi_list>" . $listObject . "</csapi_list>";

	return(new ChangeSynergy::apiListObject(ChangeSynergy::util::callCsapi($aUser, $xmlData), $self->{globals}->{LIST_TYPE}));
}

sub GetDataListBox
{
	my $self		= shift;
	my $aUser		= shift;
	my $listObject  = undef;
	my $configType  = undef;
	
	if(@_ == 1)
	{
		$listObject  = shift;
		$configType  = $self->{globals}->{SYSTEM_CONFIG};
	}
	elsif(@_ == 2)
	{
		$listObject  = shift;
		$configType  = shift;	
	}

	my $xmlData		= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>GetDataListbox</csapi_action_flag>";
	$xmlData .= "<csapi_encoded_password>false</csapi_encoded_password>";

	$xmlData .= "<csapi_token>"		   . $aUser->getUserToken()    . "</csapi_token>";
	$xmlData .= "<csapi_role>"		   . $aUser->getUserRole()     . "</csapi_role>";
	$xmlData .= "<csapi_password>"	   . $aUser->getUserPassword() . "</csapi_password>";
	$xmlData .= "<csapi_database>"	   . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		   . $aUser->getUserName()     . "</csapi_user>";
	$xmlData .= "<csapi_profile_type>" . $configType               . "</csapi_profile_type>";

	$xmlData .= "<csapi_datalistbox>" . $listObject . "</csapi_datalistbox>";

	return(new ChangeSynergy::apiListObject(ChangeSynergy::util::callCsapi($aUser, $xmlData), $self->{globals}->{DATALISTBOX_TYPE}));
}

sub GetReport
{
	my $self		= shift;
	my $aUser		= shift;
	my $listObject  = undef;
	my $configType  = undef;
	
	if(@_ == 1)
	{
		$listObject  = shift;
		$configType  = $self->{globals}->{SYSTEM_CONFIG};
	}
	elsif(@_ == 2)
	{
		$listObject  = shift;
		$configType  = shift;	
	}

	my $xmlData		= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>GetReport</csapi_action_flag>";
	$xmlData .= "<csapi_encoded_password>false</csapi_encoded_password>";

	$xmlData .= "<csapi_token>"		   . $aUser->getUserToken()    . "</csapi_token>";
	$xmlData .= "<csapi_role>"		   . $aUser->getUserRole()     . "</csapi_role>";
	$xmlData .= "<csapi_password>"	   . $aUser->getUserPassword() . "</csapi_password>";
	$xmlData .= "<csapi_database>"	   . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		   . $aUser->getUserName()     . "</csapi_user>";
	$xmlData .= "<csapi_profile_type>" . $configType               . "</csapi_profile_type>";
	
	$xmlData .= "<csapi_report>" . $listObject . "</csapi_report>";

	return(new ChangeSynergy::apiListObject(ChangeSynergy::util::callCsapi($aUser, $xmlData), $self->{globals}->{REPORT_TYPE}));
}

sub GetQuery
{
	my $self		= shift;
	my $aUser		= shift;
	my $listObject  = undef;
	my $configType  = undef;
	
	if(@_ == 1)
	{
		$listObject  = shift;
		$configType  = $self->{globals}->{SYSTEM_CONFIG};
	}
	elsif(@_ == 2)
	{
		$listObject  = shift;
		$configType  = shift;	
	}

	my $xmlData		= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>GetQuery</csapi_action_flag>";
	$xmlData .= "<csapi_encoded_password>false</csapi_encoded_password>";

	$xmlData .= "<csapi_token>"		   . $aUser->getUserToken()    . "</csapi_token>";
	$xmlData .= "<csapi_role>"		   . $aUser->getUserRole()     . "</csapi_role>";
	$xmlData .= "<csapi_password>"	   . $aUser->getUserPassword() . "</csapi_password>";
	$xmlData .= "<csapi_database>"	   . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		   . $aUser->getUserName()     . "</csapi_user>";
	$xmlData .= "<csapi_profile_type>" . $configType               . "</csapi_profile_type>";
	
	$xmlData .= "<csapi_query>" . $listObject . "</csapi_query>";

	return(new ChangeSynergy::apiListObject(ChangeSynergy::util::callCsapi($aUser, $xmlData), $self->{globals}->{REPORT_TYPE}));
}

###########################################################
## Administrative Methods
###########################################################

sub setUpConnection
{
	my $self		= shift;
	my $protocol	= shift;
	my $host		= shift;
	my $port		= shift;

	if(!defined($protocol))
	{
		die "Cannot establish internet connection with provided parameters";
	}

	if(!defined($host))
	{
		die "Cannot establish internet connection with provided parameters";
	}

	if(!defined($port))
	{
		die "Cannot establish internet connection with provided parameters";
	}

	ChangeSynergy::util::setProtocol($protocol);
	ChangeSynergy::util::setPort($port);
	ChangeSynergy::util::setHost($host);
}

sub setReportConfigType
{
	my $self		= shift;
	my $configType	= shift;

	if(!defined($configType))
	{
		die "configType is undef.";
	}
	
	ChangeSynergy::util::setReportConfigType($configType);
}

sub setQueryConfigType
{
	my $self		= shift;
	my $configType	= shift;

	if(!defined($configType))
	{
		die "configType is undef.";
	}
	
	ChangeSynergy::util::setQueryConfigType($configType);
}


sub Login
{
	my $self		= shift;
	my $user		= shift;
	my $password	= shift;
	my $role		= shift;
	my $database	= shift;
	my $aUser		= undef;
	my $xmlData		= "";

	$aUser = new ChangeSynergy::apiUser($user, $password, $role, $database);

	$xmlData .= "<csapi_action_flag>login</csapi_action_flag>";
	$xmlData .= "<csapi_encoded_password>false</csapi_encoded_password>";

	$xmlData .= "<csapi_user>"		. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_password>"	. $aUser->getUserPassword() . "</csapi_password>";
	$xmlData .= "<csapi_role>"		. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"	. $aUser->getUserDatabase() . "</csapi_database>";

	my $token = (ChangeSynergy::util::callCsapi($aUser, $xmlData));

	$aUser->setUserToken($token);

	return $aUser;
}

sub AddUser
{
	my $self		= shift;
	my $aUser		= shift;
	my $aNewUser	= shift;
	my $xmlData		= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	if(!defined($aNewUser))
	{
		die "New user information object is undef";
	}

	$xmlData .= "<csapi_action_flag>AddUser</csapi_action_flag>";
	$xmlData .= "<csapi_encoded_password>false</csapi_encoded_password>";

	$xmlData .= "<csapi_token>"		. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_user>"		. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_password>"	. $aUser->getUserPassword() . "</csapi_password>";
	$xmlData .= "<csapi_role>"		. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"	. $aUser->getUserDatabase() . "</csapi_database>";

	$xmlData .= "<csapi_adduser_user>"		. $aNewUser->getUserName()		. "</csapi_adduser_user>";
	$xmlData .= "<csapi_adduser_password>"	. $aNewUser->getUserPassword()	. "</csapi_adduser_password>";
	$xmlData .= "<csapi_adduser_role>"		. $aNewUser->getUserRole()		. "</csapi_adduser_role>";
	$xmlData .= "<csapi_adduser_database>"	. $aNewUser->getUserDatabase()	. "</csapi_adduser_database>";

	return (new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub AddUsers
{
	#Had to create this differently since we are being passed in an array of object.
	#perl does weird things when passing arrays and hashes around.
	my ($self, $aUser, $aNewUser, $iCount) = @_;

	#get the real array back from the reference.
	my @aNewUser	= @$aNewUser;
	my $xmlData		= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	if(!@aNewUser)
	{
		die "New users information object is undef";
	}

	if((!defined($iCount)) || ($iCount <=0))
	{
		die "Count must be set when adding users";
	}

	$xmlData .= "<csapi_action_flag>AddUsers</csapi_action_flag>";
	$xmlData .= "<csapi_encoded_password>false</csapi_encoded_password>";

	$xmlData .= "<csapi_token>"		. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_user>"		. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_password>"	. $aUser->getUserPassword() . "</csapi_password>";
	$xmlData .= "<csapi_role>"		. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"	. $aUser->getUserDatabase() . "</csapi_database>";

	$xmlData .= "<csapi_new_user_count>" . $iCount . "</csapi_new_user_count>";

	for(my $i = 0; $i < $iCount; $i++)
	{
		$xmlData .= "<csapi_new_user>";
			$xmlData .= "<csapi_adduser_user>"		. $aNewUser[$i]->getUserName()		. "</csapi_adduser_user>";
			$xmlData .= "<csapi_adduser_password>"	. $aNewUser[$i]->getUserPassword()	. "</csapi_adduser_password>";
			$xmlData .= "<csapi_adduser_role>"		. $aNewUser[$i]->getUserRole()		. "</csapi_adduser_role>";
			$xmlData .= "<csapi_adduser_database>"	. $aNewUser[$i]->getUserDatabase()	. "</csapi_adduser_database>";
		$xmlData .= "</csapi_new_user>";
	}

	return (new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub GetDOORSAttribute
{
	my $self           = shift;
	my $aUser          = shift;
	my $Cvid           = shift;
	my $attributeValue = shift;
	my $attributeTag   = shift;
	my $objectType     = shift;
	my $charSet        = shift;
	my $xmlData        = "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>get_DOORS_attribute</csapi_action_flag>";
	
	$xmlData .= "<csapi_token>"		. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"		. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"	. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		. $aUser->getUserName()		. "</csapi_user>";
	
	$xmlData .= "<csapi_cvid>"          . $Cvid           . "</csapi_cvid>";
	$xmlData .= "<csapi_keyname>"       . $attributeValue . "</csapi_keyname>";
	$xmlData .= "<csapi_attribute_flag>". $attributeTag   . "</csapi_attribute_flag>";
	$xmlData .= "<csapi_keyvalue>"      . $objectType     . "</csapi_keyvalue>";
	$xmlData .= "<csapi_preferenceName>". $charSet        . "</csapi_preferenceName>";

	return (new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

####################################################################
## Any basic form type
####################################################################

sub LoadFormHtml
{
	my $self		 = shift;
	my $aUser		 = shift;
	my $templateName = shift;
	my $templateType = shift;
	my $xmlData		= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_template_flag>"	. $templateName . "</csapi_template_flag>";
	$xmlData .= "<csapi_action_flag>"	. $templateType . "</csapi_action_flag>";

	return (new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub LoadFormUrl
{
	my $self		 = shift;
	my $aUser		 = shift;
	my $templateName = shift;
	my $templateType = shift;
	my $retData		 = "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$retData .= $ChangeSynergy::util::protocol;
	$retData .= "://";
	$retData .= $ChangeSynergy::util::host;
	$retData .= ":";
	$retData .= $ChangeSynergy::util::port;
	$retData .= "/servlet/PTweb";
	$retData .= "?ACTION_FLAG=";
	$retData .= ChangeSynergy::util::escape($templateType);
	$retData .= "&TEMPLATE_FLAG=";
	$retData .= ChangeSynergy::util::escape($templateName);
	$retData .= "&user=";
	$retData .= ChangeSynergy::util::escape($aUser->getUserName());
	$retData .= "&token=";
	$retData .= ChangeSynergy::util::escape($aUser->getUserToken());
	$retData .= "&role=";
	$retData .= ChangeSynergy::util::escape($aUser->getUserRole());
	$retData .= "&database=";
	$retData .= ChangeSynergy::util::escape($aUser->getUserDatabase());

	return (new ChangeSynergy::apiData($retData));
}

####################################################################
## Query and Report
####################################################################

sub QueryHtml
{
	my $self		 = shift;
	my $aUser		 = shift;
	my $reportName	 = shift;
	my $queryString	 = shift;
	my $queryName	 = shift;
	my $reportTitle	 = shift;
	my $templateName = shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(ChangeSynergy::util::QueryHtmlBase($aUser, "query", $reportName, $queryString, $queryName, $reportTitle,
					     $templateName, undef));
}

sub QueryData
{
	my $self			= shift;
	my $aUser			= shift;
	my $reportName		= shift;
	my $queryString		= shift;
	my $queryName		= shift;
	my $reportTitle		= shift;
	my $templateName	= shift;
	my $attributeList	= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	if(!defined($attributeList))
	{
		return(new ChangeSynergy::apiQueryData(ChangeSynergy::util::QueryHtmlBaseStr($aUser, "data_report", $reportName, $queryString, $queryName, 
							$reportTitle, $templateName, undef)));
	}
	else
	{
		return(new ChangeSynergy::apiQueryData(ChangeSynergy::util::QueryHtmlBaseStr($aUser, "data_report", $reportName, $queryString, $queryName,
			$reportTitle, $templateName, $attributeList)));
	}
}

sub QueryStringData
{
	my $self		 = shift;
	my $aUser		 = shift;
	my $reportName	 = shift;
	my $queryString	 = shift;
	my $attributeList = shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(new ChangeSynergy::apiQueryData(ChangeSynergy::util::QueryHtmlBaseStr($aUser, "data_report", $reportName, $queryString, undef, undef, undef, $attributeList)));
}

sub QueryNameData
{
	my $self		 = shift;
	my $aUser		 = shift;
	my $reportName	 = shift;
	my $queryName	 = shift;
	my $attributeList = shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(new ChangeSynergy::apiQueryData(ChangeSynergy::util::QueryHtmlBaseStr($aUser, "data_report", $reportName, undef, $queryName, undef, undef, $attributeList)));
}

sub ImmediateQueryHtml
{
	my $self		 = shift;
	my $aUser		 = shift;
	my $reportName	 = shift;
	my $queryString	 = shift;
	my $queryName	 = shift;
	my $reportTitle	 = shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(ChangeSynergy::util::QueryHtmlBase($aUser, "immediate_report", $reportName, $queryString, $queryName, $reportTitle, undef, undef));
}

sub ReportHtml
{
	my $self		 = shift;
	my $aUser		 = shift;
	my $reportName	 = shift;
	my $reportTitle  = shift;
	my $templateName = shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(ChangeSynergy::util::QueryHtmlBase($aUser, "report", $reportName, undef, undef, $reportTitle, $templateName, undef));
}

sub ReportData
{
	my $self		 = shift;

	if(@_ == 3)
	{
		my $aUser			= shift;
		my $reportName		= shift;
		my $attributeList	= shift;

		if(!defined($aUser))
		{
			die "User information object is undef";
		}

		return(new ChangeSynergy::apiQueryData(ChangeSynergy::util::QueryHtmlBaseStr($aUser, "data_report", $reportName,  undef, undef, undef, undef, $attributeList)));
	}
	elsif(@_ >= 4)
	{
		my $aUser		 = shift;
		my $reportName	 = shift;
		my $reportTitle  = shift;
		my $templateName = shift;
		my $attributeList	= shift;

		if(!defined($aUser))
		{
			die "User information object is undef";
		}

		if(!defined($attributeList))
		{
			return(new ChangeSynergy::apiQueryData(ChangeSynergy::util::QueryHtmlBaseStr($aUser, "data_report", $reportName, undef, undef, $reportTitle, $templateName, undef)));
		}
		else
		{
			return(new ChangeSynergy::apiQueryData(ChangeSynergy::util::QueryHtmlBaseStr($aUser, "data_report", $reportName, undef, undef, $reportTitle, $templateName, $attributeList)));
		}
	}
}

sub ImmediateReportHtml
{
	my $self		 = shift;
	my $aUser		 = shift;
	my $reportName	 = shift;
	my $reportTitle	 = shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(ChangeSynergy::util::QueryHtmlBase($aUser, "immediate_report", $reportName, undef, undef, $reportTitle, undef, undef));
}

sub ReportOnCRHtml
{
	my $self			= shift;
	my $aUser			= shift;
	my $problemNumber	= shift;
	my $reportName		= shift;
	my $reportTitle		= shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(ChangeSynergy::util::QueryHtmlBase($aUser, "problemreport", $reportName, "problem_number='" . $problemNumber ."'", undef, $reportTitle, undef, undef));
}

sub ReportOnCRData
{
	my $self			= shift;
	my $aUser			= shift;
	my $problemNumber	= shift;
	my $reportName		= shift;
	my $reportTitle		= shift;
	my $attributeList	= shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	if(!defined($attributeList))
	{
		return(new ChangeSynergy::apiQueryData(ChangeSynergy::util::QueryHtmlBaseStr($aUser, "data_report", $reportName, "problem_number='" . $problemNumber ."'", undef, $reportTitle, undef, undef)));
	}
	else
	{
		return(new ChangeSynergy::apiQueryData(ChangeSynergy::util::QueryHtmlBaseStr($aUser, "data_report", $reportName, "problem_number='" . $problemNumber ."'", undef, $reportTitle, undef, $attributeList)));
	}
}

sub ReportOnTaskHtml
{
	my $self			= shift;
	my $aUser			= shift;
	my $taskNumber		= shift;
	my $reportName		= shift;
	my $reportTitle		= shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(ChangeSynergy::util::QueryHtmlBase($aUser, "taskreport", $reportName, "task_number='" . $taskNumber ."'", undef, $reportTitle, undef, undef));
}

sub ReportOnTaskData
{
	my $self			= shift;
	my $aUser			= shift;
	my $taskNumber		= shift;
	my $reportName		= shift;
	my $reportTitle		= shift;
	my $attributeList	= shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	if(!defined($attributeList))
	{
		return(new ChangeSynergy::apiQueryData(ChangeSynergy::util::QueryHtmlBaseStr($aUser, "data_report", $reportName, "task_number='" . $taskNumber ."'", undef, $reportTitle, undef, undef)));
	}
	else
	{
		return(new ChangeSynergy::apiQueryData(ChangeSynergy::util::QueryHtmlBaseStr($aUser, "data_report", $reportName, "task_number='" . $taskNumber ."'", undef, $reportTitle, undef, $attributeList)));
	}
}

sub ReportOnObjectHtml
{
	my $self			= shift;
	my $aUser			= shift;
	my $objectId		= shift;
	my $reportName		= shift;
	my $reportTitle		= shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(ChangeSynergy::util::QueryHtmlBase($aUser, "objectreport", $reportName, "cvid='" . $objectId ."'", undef, $reportTitle, undef, undef));
}

sub ReportOnObjectData
{
	my $self			= shift;
	my $aUser			= shift;
	my $objectId		= shift;
	my $reportName		= shift;
	my $reportTitle		= shift;
	my $attributeList	= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	if(!defined($attributeList))
	{
		return(new ChangeSynergy::apiQueryData(ChangeSynergy::util::QueryHtmlBaseStr($aUser, "data_report", $reportName, "cvid='" . $objectId ."'", undef, $reportTitle, undef, undef)));
	}
	else
	{
		return(new ChangeSynergy::apiQueryData(ChangeSynergy::util::QueryHtmlBaseStr($aUser, "data_report", $reportName, "cvid='" . $objectId ."'", undef, $reportTitle, undef, $attributeList)));
	}
}

####################################################################
## Framesets
####################################################################

sub LoadFrameSetHtml
{
	my $self			= shift;
	my $aUser			= shift;
	my $templateName	= shift;
	my $taskNumber		= shift;
	my $taskStatus		= shift;
	my $problemNumber	= shift;
	my $problemStatus	= shift;
	my $cvid			= shift;
	my $externalData	= shift;
	my $xmlData			= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>frameset_form</csapi_action_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_template_flag>"	. $templateName				. "</csapi_template_flag>";

	if(defined($taskNumber))
	{
		$xmlData .= "<csapi_task_id>" . $taskNumber . "</csapi_task_id>";
	}

	if(defined($taskStatus))
	{
		$xmlData .= "<csapi_task_status>" . $taskStatus . "</csapi_task_status>";
	}

	if(defined($problemNumber))
	{
		$xmlData .= "<csapi_cr_id>" . $problemNumber . "</csapi_cr_id>";
	}

	if(defined($problemStatus))
	{
		$xmlData .= "<csapi_cr_status>" . $problemStatus . "</csapi_cr_status>";
	}

	if(defined($cvid))
	{
		$xmlData .= "<csapi_object_id>" . $cvid . "</csapi_object_id>";
	}

	if(defined($externalData))
	{
		$xmlData .= "<csapi_external_data>" . $externalData . "</csapi_external_data>";
	}

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub LoadFrameSetUrl
{
	my $self			= shift;
	my $aUser			= shift;
	my $templateName	= shift;
	my $taskNumber		= shift;
	my $taskStatus		= shift;
	my $problemNumber	= shift;
	my $problemStatus	= shift;
	my $cvid			= shift;
	my $externalData	= shift;
	my $retData			= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$retData .= $ChangeSynergy::util::protocol;
	$retData .= "://";
	$retData .= $ChangeSynergy::util::host;
	$retData .= ":";
	$retData .= $ChangeSynergy::util::port;
	$retData .= "/servlet/PTweb";
	$retData .= "?ACTION_FLAG=frameset_form";
	$retData .= "&TEMPLATE_FLAG=";
	$retData .= ChangeSynergy::util::escape($templateName);
	$retData .= "&user=";
	$retData .= ChangeSynergy::util::escape($aUser->getUserName());
	$retData .= "&token=";
	$retData .= ChangeSynergy::util::escape($aUser->getUserToken());
	$retData .= "&role=";
	$retData .= ChangeSynergy::util::escape($aUser->getUserRole());
	$retData .= "&database=";
	$retData .= ChangeSynergy::util::escape($aUser->getUserDatabase());

	if(defined($taskNumber))
	{
		$retData .= "&task_number=";
		$retData .= ChangeSynergy::util::escape($taskNumber);
	}

	if(defined($taskStatus))
	{
		$retData .= "&status=";
		$retData .= ChangeSynergy::util::escape($taskStatus);
	}

	if(defined($problemNumber))
	{
		$retData .= "&problem_number=";
		$retData .= ChangeSynergy::util::escape($problemNumber);
	}

	if(defined($problemStatus))
	{
		$retData .= "&crstatus=";
		$retData .= ChangeSynergy::util::escape($problemStatus);
	}

	if(defined($cvid))
	{
		$retData .= "&cvid=";
		$retData .= ChangeSynergy::util::escape($cvid);
	}

	if(defined($externalData))
	{
		$retData .= "&EXTERNAL_CONTEXT_DATA=";
		$retData .= ChangeSynergy::util::escape($externalData);
	}

	return(new ChangeSynergy::apiData($retData));
}

####################################################################
## Relation Create
####################################################################

sub CreateMiscObject
{
	my $self			= shift;
	my $aUser			= shift;
	my $objectString	= shift;
	my $xmlData			= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>CreateMiscObject</csapi_action_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_action_item>"	. $objectString				. "</csapi_action_item>";

	my $tmp = ChangeSynergy::util::callCsapi($aUser, $xmlData);
	my $iStart = index($tmp, $self->{globals}->{BGN_CSAPI_CVID});
	my $iEnd   = index($tmp, $self->{globals}->{END_CSAPI_CVID});

	if(($iStart < 0) || ($iEnd < 0))
	{
		die "Cannot parse CVID";
	}

	$iStart += length($self->{globals}->{BGN_CSAPI_CVID});

	if(($iStart == $iEnd) || ($iStart > $iEnd))
	{
		die "Cannot parse CVID";
	}

	return(new ChangeSynergy::apiData(substr($tmp, $iStart, $iEnd - $iStart)));
}

sub CreateRelation
{
	my $self				= shift;
	my $aUser				= shift;
	my $bothWayRelationship	= shift;
	my $fromObject			= shift;
	my $toObject			= shift;
	my $relationName		= shift;
	my $relationType		= shift;
	my $xmlData			= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>CreateRelation</csapi_action_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";

	$xmlData .= "<csapi_relation_flag>"	. $relationName			. "</csapi_relation_flag>";
	$xmlData .= "<csapi_to_object>"		. $toObject				. "</csapi_to_object>";
	$xmlData .= "<csapi_from_object>"	. $fromObject			. "</csapi_from_object>";
	$xmlData .= "<csapi_relation_type>"	. $relationType			. "</csapi_relation_type>";

	if($bothWayRelationship eq "true")
	{
		$xmlData .= "<csapi_both_way_relationship>true</csapi_both_way_relationship>";
	}
	else
	{
		$xmlData .= "<csapi_both_way_relationship>false</csapi_both_way_relationship>";
	}

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub DeleteRelation
{
	my $self				= shift;
	my $aUser				= shift;
	my $bothWayRelationship	= shift;
	my $fromObject			= shift;
	my $toObject			= shift;
	my $relationName		= shift;
	my $relationType		= shift;
	my $xmlData			= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>DeleteRelation</csapi_action_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";

	$xmlData .= "<csapi_relation_flag>"	. $relationName			. "</csapi_relation_flag>";
	$xmlData .= "<csapi_to_object>"		. $toObject				. "</csapi_to_object>";
	$xmlData .= "<csapi_from_object>"	. $fromObject			. "</csapi_from_object>";
	$xmlData .= "<csapi_relation_type>"	. $relationType			. "</csapi_relation_type>";

	if($bothWayRelationship eq "true")
	{
		$xmlData .= "<csapi_both_way_relationship>true</csapi_both_way_relationship>";
	}
	else
	{
		$xmlData .= "<csapi_both_way_relationship>false</csapi_both_way_relationship>";
	}

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

####################################################################
## Change Requests
####################################################################

sub ModifyCR
{
	my $self	= shift;
	my $aUser	= shift;
	my $lpData	= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(new ChangeSynergy::apiData(ChangeSynergy::util::ModifyShowAction($aUser, $lpData, "CRModify")));
}

sub TransitionCR
{
	my $self	= shift;
	my $aUser	= shift;
	my $lpData	= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(new ChangeSynergy::apiData(ChangeSynergy::util::ModifyShowAction($aUser, $lpData, "CRTransition")));
}

sub SubmitCR
{
	my $self	= shift;
	my $aUser	= shift;
	my $lpData	= shift;

	return(new ChangeSynergy::apiData(ChangeSynergy::util::ModifySubmitAction($aUser, $lpData, "CRSubmit")));
}

sub SubmitCRAssocCR
{
	my $self			= shift;
	my $aUser			= shift;
	my $lpData			= shift;
	my $relationName	= shift;
	my $problemNumber	= shift;
	
	return(new ChangeSynergy::apiData(ChangeSynergy::util::ModifySubmitAssocAction($aUser, $lpData, "CRSubmitCRAssoc", $relationName, $problemNumber)));
}

sub AttributeModifyCRData
{
	my $self			= shift;
	my $aUser			= shift;
	my $problem_number	= shift;
	my $attributeName	= shift;
	my $xmlData			= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	if(!defined($attributeName))
	{
		$attributeName = "crstatus";
	}

	$xmlData .= "<csapi_action_flag>PreCRAttrModify</csapi_action_flag>";
	$xmlData .= "<csapi_all_transitions>false</csapi_all_transitions>";
	$xmlData .= "<csapi_template_flag>" . $attributeName			. "</csapi_template_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";	
	$xmlData .= "<csapi_cr_id>"			. $problem_number			. "</csapi_cr_id>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub AttributeModifyCRDataAllTransitions
{
	my $self          = shift;
	my $aUser = shift;
	my $ProblemNumber = shift;
	my $AttributeName = shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	if(!defined($AttributeName))
	{
		$AttributeName = "crstatus";
	}

	my $xmlData = "";
	
	$xmlData .= "<csapi_action_flag>PreCRAttrModify</csapi_action_flag>";
	$xmlData .= "<csapi_all_transitions>true</csapi_all_transitions>";
	$xmlData .= "<csapi_template_flag>" . $AttributeName			           . "</csapi_template_flag>";
	$xmlData .= "<csapi_token>"         . $aUser->getUserToken()		       . "</csapi_token>";
	$xmlData .= "<csapi_role>"          . $aUser->getUserRole()				   . "</csapi_role>";
	$xmlData .= "<csapi_database>"      . $aUser->getUserDatabase()			   . "</csapi_database>";
	$xmlData .= "<csapi_user>"          . $aUser->getUserName()			       . "</csapi_user>";
	$xmlData .= "<csapi_cr_id>"         . $ProblemNumber					   . "</csapi_cr_id>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub ModifyCRData
{
	my $self			= shift;
	my $aUser			= shift;
	my $problem_number	= shift;
	my $templateName	= shift;
	my $xmlData			= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>PreCRModify</csapi_action_flag>";
	$xmlData .= "<csapi_all_transitions>false</csapi_all_transitions>";
	$xmlData .= "<csapi_template_flag>" . $templateName				. "</csapi_template_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";	
	$xmlData .= "<csapi_cr_id>"			. $problem_number			. "</csapi_cr_id>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub ModifyCRDataAllTransitions
{
	my $self          = shift;
	my $aUser = shift;
	my $ProblemNumber = shift;
	my $TemplateName = shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}


	my $xmlData = "";
	
	$xmlData .= "<csapi_action_flag>PreCRModify</csapi_action_flag>";
	$xmlData .= "<csapi_all_transitions>true</csapi_all_transitions>";
	$xmlData .= "<csapi_template_flag>" . $TemplateName				   . "</csapi_template_flag>";
	$xmlData .= "<csapi_token>"         . $aUser->getUserToken()       . "</csapi_token>";
	$xmlData .= "<csapi_role>"          . $aUser->getUserRole()        . "</csapi_role>";
	$xmlData .= "<csapi_database>"      . $aUser->getUserDatabase()    . "</csapi_database>";
	$xmlData .= "<csapi_user>"          . $aUser->getUserName()        . "</csapi_user>";
	$xmlData .= "<csapi_cr_id>"         . $ProblemNumber               . "</csapi_cr_id>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub GetCRData
{
	my $self			= shift;
	my $aUser			= shift;
	my $problem_number	= shift;
	my $attributeList	= shift;
	my $xmlData			= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>PreCRModify</csapi_action_flag>";
	$xmlData .= "<csapi_all_transitions>false</csapi_all_transitions>";
	$xmlData .= "<csapi_attribute_flag>"	. $attributeList				. "</csapi_attribute_flag>";
	$xmlData .= "<csapi_token>"				. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"				. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"			. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"				. $aUser->getUserName()		. "</csapi_user>";	
	$xmlData .= "<csapi_cr_id>"				. $problem_number			. "</csapi_cr_id>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub GetCRDataAllTransitions
{
	my $self          = shift;
	my $aUser		  = shift;
	my $ProblemNumber = shift;
	my $AttributeList = shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	my $xmlData = "";
	
	$xmlData .= "<csapi_action_flag>PreCRModify</csapi_action_flag>";
	$xmlData .= "<csapi_all_transitions>true</csapi_all_transitions>";
	$xmlData .= "<csapi_attribute_flag>". $AttributeList           . "</csapi_attribute_flag>";
	$xmlData .= "<csapi_token>"         . $aUser->getUserToken()       . "</csapi_token>";
	$xmlData .= "<csapi_role>"          . $aUser->getUserRole()        . "</csapi_role>";
	$xmlData .= "<csapi_database>"      . $aUser->getUserDatabase()    . "</csapi_database>";
	$xmlData .= "<csapi_user>"          . $aUser->getUserName()        . "</csapi_user>";
	$xmlData .= "<csapi_cr_id>"         . $ProblemNumber           . "</csapi_cr_id>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}



sub TransitionCRData
{
	my $self			= shift;
	my $aUser			= shift;
	my $problem_number	= shift;
	my $templateName	= shift;
	my $xmlData			= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>PreCRTransition</csapi_action_flag>";
	$xmlData .= "<csapi_template_flag>"  . $templateName				. "</csapi_template_flag>";
	$xmlData .= "<csapi_token>"				. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"				. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"			. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"				. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_cr_id>"				. $problem_number			. "</csapi_cr_id>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub CopyCRData
{
	my $self			= shift;
	my $aUser			= shift;
	my $problemNumber	= shift;
	my $templateName	= shift;
	my $xmlData			= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>PreCRCopy</csapi_action_flag>";
	$xmlData .= "<csapi_template_flag>"	. $templateName				. "</csapi_template_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_cr_id>"			. $problemNumber			. "</csapi_cr_id>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub SubmitCRData
{
	my $self			= shift;
	my $aUser			= shift;
	my $templateName	= shift;
	my $xmlData			= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>PreCRSubmit</csapi_action_flag>";
	$xmlData .= "<csapi_template_flag>"	. $templateName				. "</csapi_template_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub SubmitCRHtml
{
	my $self			= shift;
	my $aUser			= shift;
	my $templateName	= shift;
	my $problemNumber   = shift;
	my $relationName	= shift;
	my $externalData	= shift;
	my $xmlData			= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>problem_submit_form</csapi_action_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_template_flag>"	. $templateName				. "</csapi_template_flag>";

	if(defined($problemNumber))
	{
		$xmlData .= "<csapi_cr_id>" . $problemNumber . "</csapi_cr_id>";
	}

	if(defined($relationName))
	{
		$xmlData .= "<csapi_relation_flag>" . $relationName . "</csapi_relation_flag>";
	}

	if(defined($externalData))
	{
		$xmlData .= "<csapi_external_data>" . $externalData . "</csapi_external_data>";
	}

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub SubmitCRUrl
{
	my $self			= shift;
	my $aUser			= shift;
	my $templateName	= shift;
	my $problemNumber   = shift;
	my $relationName	= shift;
	my $externalData	= shift;
	my $retData			= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$retData .= $ChangeSynergy::util::protocol;
	$retData .= "://";
	$retData .= $ChangeSynergy::util::host;
	$retData .= ":";
	$retData .= $ChangeSynergy::util::port;
	$retData .= "/servlet/PTweb";
	$retData .= "?ACTION_FLAG=problem_submit_form";
	$retData .= "&TEMPLATE_FLAG=";
	$retData .= ChangeSynergy::util::escape($templateName);
	$retData .= "&user=";
	$retData .= ChangeSynergy::util::escape($aUser->getUserName());
	$retData .= "&token=";
	$retData .= ChangeSynergy::util::escape($aUser->getUserToken());
	$retData .= "&role=";
	$retData .= ChangeSynergy::util::escape($aUser->getUserRole());
	$retData .= "&database=";
	$retData .= ChangeSynergy::util::escape($aUser->getUserDatabase());

	if(defined($problemNumber))
	{
		$retData .= "&problem_number=";
		$retData .=  ChangeSynergy::util::escape($problemNumber);
	}

	if(defined($relationName))
	{
		$retData .= "&RELATION_NAME=";
		$retData .=  ChangeSynergy::util::escape($relationName);
	}

	if(defined($externalData))
	{
		$retData .= "&EXTERNAL_CONTEXT_DATA=";
		$retData .=  ChangeSynergy::util::escape($externalData);
	}

	return(new ChangeSynergy::apiData($retData));
}

sub ShowCRHtml
{
	my $self			= shift;

	if(@_ == 4)
	{
		my $aUser			= shift;
		my $problemNumber	= shift;
		my $relationName	= shift;
		my $isModifiable	= shift;
		my $xmlData			= "";	

		if(!defined($aUser))
		{
			die "User information object is undef";
		}

		$xmlData .= "<csapi_action_flag>problem_attr_show_form</csapi_action_flag>";
		$xmlData .= "<csapi_template_flag>crstatus</csapi_template_flag>";
		$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
		$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
		$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
		$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";

		if(defined($problemNumber))
		{
			$xmlData .= "<csapi_cr_id>" . $problemNumber . "</csapi_cr_id>";
		}

		if(defined($isModifiable))
		{
			$xmlData .= "<csapi_is_modifiable>" . $isModifiable . "</csapi_is_modifiable>";
		}

		return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
	}
	else
	{
		my $aUser			= shift;
		my $problemNumber	= shift;
		my $templateName	= shift;
		my $relationName	= shift;
		my $isModifiable	= shift;
		my $xmlData			= "";

		if(!defined($aUser))
		{
			die "User information object is undef";
		}

		$xmlData .= "<csapi_action_flag>problem_show_form</csapi_action_flag>";
		$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
		$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
		$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
		$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";
		$xmlData .= "<csapi_template_flag>"	. $templateName				. "</csapi_template_flag>";
		$xmlData .= "<csapi_cr_id>"			. $problemNumber			. "</csapi_cr_id>";

		if(defined($relationName))
		{
			$xmlData .= "<csapi_relation_flag>" . $relationName . "</csapi_relation_flag>";
		}

		if(defined($isModifiable))
		{
			$xmlData .= "<csapi_is_modifiable>" . $isModifiable . "</csapi_is_modifiable>";
		}

		return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
	}
}

sub ShowCRUrl
{
	my $self			= shift;

	if(@_ == 4)
	{
		my $aUser			= shift;
		my $problemNumber	= shift;
		my $relationName	= shift;
		my $isModifiable	= shift;
		my $retData			= "";	

		if(!defined($aUser))
		{
			die "User information object is undef";
		}

		$retData .= $ChangeSynergy::util::protocol;
		$retData .= "://";
		$retData .= $ChangeSynergy::util::host;
		$retData .= ":";
		$retData .= $ChangeSynergy::util::port;
		$retData .= "/servlet/PTweb";
		$retData .= "?ACTION_FLAG=problem_attr_show_form";
		$retData .= "&TEMPLATE_FLAG=crstatus";
		$retData .= "&problem_number=";
		$retData .= ChangeSynergy::util::escape($problemNumber);
		$retData .= "&user=";
		$retData .= ChangeSynergy::util::escape($aUser->getUserName());
		$retData .= "&token=";
		$retData .= ChangeSynergy::util::escape($aUser->getUserToken());
		$retData .= "&role=";
		$retData .= ChangeSynergy::util::escape($aUser->getUserRole());
		$retData .= "&database=";
		$retData .= ChangeSynergy::util::escape($aUser->getUserDatabase());

		if(defined($relationName))
		{
			$retData .= "&RELATION_NAME=";
			$retData .= ChangeSynergy::util::escape($relationName);
		}

		if(defined($isModifiable))
		{
			$retData .= "&IS_MODIFIABLE=";
			$retData .= ChangeSynergy::util::escape($isModifiable);
		}

		return(new ChangeSynergy::apiData($retData));
	}
	else
	{
		my $aUser			= shift;
		my $problemNumber	= shift;
		my $templateName	= shift;
		my $relationName	= shift;
		my $isModifiable	= shift;
		my $retData			= "";	

		if(!defined($aUser))
		{
			die "User information object is undef";
		}

		$retData .= $ChangeSynergy::util::protocol;
		$retData .= "://";
		$retData .= $ChangeSynergy::util::host;
		$retData .= ":";
		$retData .= $ChangeSynergy::util::port;
		$retData .= "/servlet/PTweb";
		$retData .= "?ACTION_FLAG=problem_show_form";
		$retData .= "&TEMPLATE_FLAG=";
		$retData .= ChangeSynergy::util::escape($templateName);
		$retData .= "&problem_number=";
		$retData .= ChangeSynergy::util::escape($problemNumber);
		$retData .= "&user=";
		$retData .= ChangeSynergy::util::escape($aUser->getUserName());
		$retData .= "&token=";
		$retData .= ChangeSynergy::util::escape($aUser->getUserToken());
		$retData .= "&role=";
		$retData .= ChangeSynergy::util::escape($aUser->getUserRole());
		$retData .= "&database=";
		$retData .= ChangeSynergy::util::escape($aUser->getUserDatabase());

		if(defined($relationName))
		{
			$retData .= "&RELATION_NAME=";
			$retData .= ChangeSynergy::util::escape($relationName);
		}

		if(defined($isModifiable))
		{
			$retData .= "&IS_MODIFIABLE=";
			$retData .= ChangeSynergy::util::escape($isModifiable);
		}

		return(new ChangeSynergy::apiData($retData));
	}
}

####################################################################
## Tasks
####################################################################

sub ModifyTask
{
	my $self	= shift;
	my $aUser	= shift;
	my $lpData	= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(new ChangeSynergy::apiData(ChangeSynergy::util::ModifyShowAction($aUser, $lpData, "TaskModify")));
}

sub TransitionTask
{
	my $self	= shift;
	my $aUser	= shift;
	my $lpData	= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(new ChangeSynergy::apiData(ChangeSynergy::util::ModifyShowAction($aUser, $lpData, "TaskTransition")));
}

sub SubmitTask
{
	my $self	= shift;
	my $aUser	= shift;
	my $lpData	= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(new ChangeSynergy::apiData(ChangeSynergy::util::ModifySubmitAction($aUser, $lpData, "TaskSubmit")));
}

sub SubmitTaskAssocCR
{
	my $self			= shift;
	my $aUser			= shift;
	my $lpData			= shift;
	my $relationName	= shift;
	my $problemNumber	= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(new ChangeSynergy::apiData(ChangeSynergy::util::ModifySubmitAssocAction($aUser, $lpData, "TaskSubmitCRAssoc", $relationName, $problemNumber)));
}

sub AttributeModifyTaskData
{
	my $self			= shift;
	my $aUser			= shift;
	my $taskNumber		= shift;
	my $attributeName	= shift;
	my $xmlData			= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>PreTaskAttrModify</csapi_action_flag>";
	$xmlData .= "<csapi_template_flag>"	. $attributeName			. "</csapi_template_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_task_id>"		. $taskNumber				. "</csapi_task_id>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub ModifyTaskData
{
	my $self			= shift;
	my $aUser			= shift;
	my $taskNumber		= shift;
	my $templateName	= shift;
	my $xmlData			= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>PreTaskModify</csapi_action_flag>";
	$xmlData .= "<csapi_template_flag>"	. $templateName				. "</csapi_template_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_task_id>"		. $taskNumber				. "</csapi_task_id>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub GetTaskData
{
	my $self			= shift;
	my $aUser			= shift;
	my $taskNumber		= shift;
	my $attributeList	= shift;
	my $xmlData			= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>PreTaskModify</csapi_action_flag>";
	$xmlData .= "<csapi_attribute_flag>"	. $attributeList			. "</csapi_attribute_flag>";
	$xmlData .= "<csapi_token>"				. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"				. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"			. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"				. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_task_id>"			. $taskNumber				. "</csapi_task_id>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub TransitionTaskData
{
	my $self			= shift;
	my $aUser			= shift;
	my $taskNumber		= shift;
	my $templateName	= shift;
	my $xmlData			= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>PreTaskTransition</csapi_action_flag>";
	$xmlData .= "<csapi_template_flag>"		. $templateName				. "</csapi_template_flag>";
	$xmlData .= "<csapi_token>"				. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"				. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"			. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"				. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_task_id>"			. $taskNumber				. "</csapi_task_id>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub CopyTaskData
{
	my $self			= shift;
	my $aUser			= shift;
	my $taskNumber		= shift;
	my $templateName	= shift;
	my $xmlData			= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>PreTaskCopy</csapi_action_flag>";
	$xmlData .= "<csapi_template_flag>"		. $templateName				. "</csapi_template_flag>";
	$xmlData .= "<csapi_token>"				. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"				. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"			. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"				. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_task_id>"			. $taskNumber				. "</csapi_task_id>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub SubmitTaskData
{
	my $self			= shift;
	my $aUser			= shift;
	my $templateName	= shift;
	my $xmlData			= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>PreTaskSubmit</csapi_action_flag>";
	$xmlData .= "<csapi_template_flag>"		. $templateName				. "</csapi_template_flag>";
	$xmlData .= "<csapi_token>"				. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"				. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"			. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"				. $aUser->getUserName()		. "</csapi_user>";

	return(new ChangeSynergy::apiObjectVector(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub SubmitTaskHtml
{
	my $self			= shift;
	my $aUser			= shift;
	my $templateName	= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(&LoadFormHtml($self, $aUser, $templateName, "task_submit_form"));
}

sub SubmitTaskUrl
{
	my $self			= shift;
	my $aUser			= shift;
	my $templateName	= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(&LoadFormUrl($self, $aUser, $templateName, "task_submit_form"));
}

sub ShowTaskHtml
{
	my $self			= shift;

	if(@_ == 4)
	{
		my $aUser			= shift;
		my $taskNumber		= shift;
		my $relationName	= shift;
		my $isModifiable	= shift;
		my $xmlData			= shift;

		if(!defined($aUser))
		{
			die "User information object is undef";
		}

		$xmlData .= "<csapi_action_flag>task_attr_show_form</csapi_action_flag>";
		$xmlData .= "<csapi_template_flag>status</csapi_template_flag>";
		$xmlData .= "<csapi_token>"				. $aUser->getUserToken()	. "</csapi_token>";
		$xmlData .= "<csapi_role>"				. $aUser->getUserRole()		. "</csapi_role>";
		$xmlData .= "<csapi_database>"			. $aUser->getUserDatabase() . "</csapi_database>";
		$xmlData .= "<csapi_user>"				. $aUser->getUserName()		. "</csapi_user>";
		$xmlData .= "<csapi_task_id>"			. $taskNumber				. "</csapi_task_id>";

		if(defined($relationName))
		{
			$xmlData .= "<csapi_relation_flag>"	. $relationName	. "</csapi_relation_flag>";
		}

		if(defined($isModifiable))
		{
			$xmlData .= "<csapi_is_modifiable>"	. $isModifiable	. "</csapi_is_modifiable>";
		}

		return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
	}
	else
	{
		my $aUser			= shift;
		my $taskNumber		= shift;
		my $templateName	= shift;
		my $relationName	= shift;
		my $isModifiable	= shift;
		my $xmlData			= shift;

		if(!defined($aUser))
		{
			die "User information object is undef";
		}

		$xmlData .= "<csapi_action_flag>task_show_form</csapi_action_flag>";
		$xmlData .= "<csapi_template_flag>"     . $templateName				. "</csapi_template_flag>";
		$xmlData .= "<csapi_token>"				. $aUser->getUserToken()	. "</csapi_token>";
		$xmlData .= "<csapi_role>"				. $aUser->getUserRole()		. "</csapi_role>";
		$xmlData .= "<csapi_database>"			. $aUser->getUserDatabase() . "</csapi_database>";
		$xmlData .= "<csapi_user>"				. $aUser->getUserName()		. "</csapi_user>";
		$xmlData .= "<csapi_task_id>"			. $taskNumber				. "</csapi_task_id>";

		if(defined($relationName))
		{
			$xmlData .= "<csapi_relation_flag>"	. $relationName	. "</csapi_relation_flag>";
		}

		if(defined($isModifiable))
		{
			$xmlData .= "<csapi_is_modifiable>"	. $isModifiable	. "</csapi_is_modifiable>";
		}

		return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
	}
}

sub ShowTaskUrl
{
	my $self			= shift;

	if(@_ == 4)
	{
		my $aUser			= shift;
		my $taskNumber		= shift;
		my $relationName	= shift;
		my $isModifiable	= shift;
		my $retData			= shift;

		if(!defined($aUser))
		{
			die "User information object is undef";
		}

		$retData .= $ChangeSynergy::util::protocol;
		$retData .= "://";
		$retData .= $ChangeSynergy::util::host;
		$retData .= ":";
		$retData .= $ChangeSynergy::util::port;
		$retData .= "/servlet/PTweb";
		$retData .= "?ACTION_FLAG=task_attr_show_form";
		$retData .= "&TEMPLATE_FLAG=status";
		$retData .= "&task_number=";
		$retData .= ChangeSynergy::util::escape($taskNumber);
		$retData .= "&user=";
		$retData .= ChangeSynergy::util::escape($aUser->getUserName());
		$retData .= "&token=";
		$retData .= ChangeSynergy::util::escape($aUser->getUserToken());
		$retData .= "&role=";
		$retData .= ChangeSynergy::util::escape($aUser->getUserRole());
		$retData .= "&database=";
		$retData .= ChangeSynergy::util::escape($aUser->getUserDatabase());

		if(defined($relationName))
		{
			$retData .= "&RELATION_NAME=";
			$retData .= ChangeSynergy::util::escape($relationName);
		}

		if(defined($isModifiable))
		{
			$retData .= "&IS_MODIFIABLE=";
			$retData .= ChangeSynergy::util::escape($isModifiable);
		}

		return(new ChangeSynergy::apiData($retData));
	}
	else
	{
		my $aUser			= shift;
		my $taskNumber		= shift;
		my $templateName	= shift;
		my $relationName	= shift;
		my $isModifiable	= shift;
		my $retData			= shift;

		if(!defined($aUser))
		{
			die "User information object is undef";
		}

		$retData .= $ChangeSynergy::util::protocol;
		$retData .= "://";
		$retData .= $ChangeSynergy::util::host;
		$retData .= ":";
		$retData .= $ChangeSynergy::util::port;
		$retData .= "/servlet/PTweb";
		$retData .= "?ACTION_FLAG=task_show_form";
		$retData .= "&TEMPLATE_FLAG=";
		$retData .= ChangeSynergy::util::escape($templateName);
		$retData .= "&task_number=";
		$retData .= ChangeSynergy::util::escape($taskNumber);
		$retData .= "&user=";
		$retData .= ChangeSynergy::util::escape($aUser->getUserName());
		$retData .= "&token=";
		$retData .= ChangeSynergy::util::escape($aUser->getUserToken());
		$retData .= "&role=";
		$retData .= ChangeSynergy::util::escape($aUser->getUserRole());
		$retData .= "&database=";
		$retData .= ChangeSynergy::util::escape($aUser->getUserDatabase());

		if(defined($relationName))
		{
			$retData .= "&RELATION_NAME=";
			$retData .= ChangeSynergy::util::escape($relationName);
		}

		if(defined($isModifiable))
		{
			$retData .= "&IS_MODIFIABLE=";
			$retData .= ChangeSynergy::util::escape($isModifiable);
		}

		return(new ChangeSynergy::apiData($retData));
	}
}

sub VerifySignatures
{
	my $self          = shift;
	my $aUser         = shift;
	my $problemNumber = shift;
	my $attributeName = shift;
	my $xmlData       = "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}
	
	$xmlData .= "<csapi_action_flag>verify_signatures</csapi_action_flag>";
	$xmlData .= "<csapi_token>"          . $aUser->getUserToken()    . "</csapi_token>";
	$xmlData .= "<csapi_role>"           . $aUser->getUserRole()     . "</csapi_role>";
	$xmlData .= "<csapi_database>"       . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"           . $aUser->getUserName()     . "</csapi_user>";
	$xmlData .= "<csapi_cr_id>"          . $problemNumber            . "</csapi_cr_id>";
	$xmlData .= "<csapi_attribute_flag>" . $attributeName            . "</csapi_attribute_flag>";
	
	my $responseData = ChangeSynergy::util::callCsapi($aUser, $xmlData);

	return ($responseData);
}

sub DeleteChangeRequest
{
	my $self          = shift;
	my $aUser         = shift;
	my $problemNumber = shift;
	my $xmlData       = "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>delete_cr</csapi_action_flag>";
	$xmlData .= "<csapi_token>"    . $aUser->getUserToken()    . "</csapi_token>";
	$xmlData .= "<csapi_role>"     . $aUser->getUserRole()     . "</csapi_role>";
	$xmlData .= "<csapi_database>" . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"     . $aUser->getUserName()     . "</csapi_user>";
	$xmlData .= "<csapi_cr_id>"    . $problemNumber            . "</csapi_cr_id>";

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub DeleteTask
{

	my $self          = shift;
	my $aUser         = shift;
	my $taskNumber = shift;
	my $xmlData       = "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>delete_task</csapi_action_flag>";
	$xmlData .= "<csapi_token>"    . $aUser->getUserToken()    . "</csapi_token>";
	$xmlData .= "<csapi_role>"     . $aUser->getUserRole()     . "</csapi_role>";
	$xmlData .= "<csapi_database>" . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"     . $aUser->getUserName()     . "</csapi_user>";
	$xmlData .= "<csapi_task_id>"  . $taskNumber               . "</csapi_task_id>";

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub ChangeRequestFullName
{
	my $self            = shift;
	my $aUser			= shift;
	my $ProblemNumber	= shift;
	my $xmlData			= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>GetCRFullName</csapi_action_flag>";
	$xmlData .= "<csapi_token>"    . $aUser->getUserToken()    . "</csapi_token>";
	$xmlData .= "<csapi_role>"     . $aUser->getUserRole()     . "</csapi_role>";
	$xmlData .= "<csapi_database>" . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"     . $aUser->getUserName()     . "</csapi_user>";
	$xmlData .= "<csapi_cr_id>"    . $ProblemNumber        . "</csapi_cr_id>";

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub TaskFullName
{
	my $self        = shift;
	my $aUser		= shift;
	my $TaskNumber	= shift;
	my $xmlData		= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}
	
	$xmlData .= "<csapi_action_flag>GetTaskFullName</csapi_action_flag>";

	$xmlData .= "<csapi_token>"    . $aUser->getUserToken()    . "</csapi_token>";
	$xmlData .= "<csapi_role>"     . $aUser->getUserRole()     . "</csapi_role>";
	$xmlData .= "<csapi_database>" . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"     . $aUser->getUserName()     . "</csapi_user>";
	$xmlData .= "<csapi_task_id>"  . $TaskNumber           . "</csapi_task_id>";
	
	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub CallBsfScript
{
	my $self = shift;
	my $aUser = shift;
	my $scriptName = shift;
	my $scriptData = shift;
	my $xmlData = "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>callScript</csapi_action_flag>";

	$xmlData .= "<csapi_token>" . $aUser->getUserToken() . "</csapi_token>";
	$xmlData .= "<csapi_role>" . $aUser->getUserRole() . "</csapi_role>";
	$xmlData .= "<csapi_database>" . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>" . $aUser->getUserName() . "</csapi_user>";
	$xmlData .= "<csapi_script_name>" . ChangeSynergy::util::xmlEncode($scriptName) . "</csapi_script_name>";
	$xmlData .= "<csapi_script_data>" . ChangeSynergy::util::xmlEncode($scriptData) . "</csapi_script_data>";

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

1;

__END__

=head1 Name

ChangeSynergy::csapi

=head1 Description

The ChangeSynergy::csapi class is the class used to send and retrieve
information from the SYNERGY/Change server.

=head1 Methods

The following methods are available:

=over 4

=cut

##############################################################################

=item B<new>

 sub new()

Initializes a newly created ChangeSynergy::csapi class.

 my $csapi = new ChangeSynergy::csapi();

=cut

##############################################################################

=item B<AddAPreferenceForAUser>

Add/Change a user preference and value for a user.  The value to be 
added or changed must already be defined as a user preference via one of 
the configuration files.  To edit or add a users cfg setting, the keyName
should be "_USER_CFG_" and the system will append the users name. 
The return result is an instance of the L<apiData> class.

Note: It is not possible to change or add user profile values.  These values
are the users first names, last names, email addresses, fax numbers, telephone
numbers and addresses.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  username: The name of the user's preferences to edit.
	scalar  keyName : The name of the preference to add.
	scalar  keyValue: The value for the preference being added.
	scalar  allDBs  : true or false, should the add take place for all databases
						or just the one that the current api user is logged into.

 Returns: apiData
	the return message from the server.
 
 Example:
	
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");
		
		$tmpData = $csapi->AddAPreferenceForAUser($aUser, "u00001", "user_fontsize", "9", "true");
	
		print $tmpData->getResponseData();

	};

	if ($@)
	{
		print $@;
	}

=cut

#############################################################################


=item B<AddAPreferenceForAllUsers>

Add/Change a user preference and value for all users.  The value to be 
added or changed must already be defined as a user preference via one of 
the configuration files.  To edit or add a users cfg setting, the keyName
should be "_USER_CFG_" and the system will append the users name. 
The return result is an instance of the L<apiData> class.

Note: It is not possible to change or add user profile values.  These values
are the users first names, last names, email addresses, fax numbers, telephone
numbers and addresses.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  keyName : The name of the preference to add.
	scalar  keyValue: The value for the preference being added.
	scalar  allDBs  : true or false, should the add take place for all databases
						or just the one that the current api user is logged into.

 Returns: apiData
	the return message from the server.
 
 Example:
	
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");
		
		$tmpData = $csapi->AddAPreferenceForAllUsers($aUser, "user_fontsize", "9", "true");
	
		print $tmpData->getResponseData();

	};

	if ($@)
	{
		print $@;
	}

=cut

#############################################################################


=item B<AddUser>

Add a new user to both the LDAP server and the CM Synergy database 
with the given set of CMSynergy roles. The new user can login in after
this call completes. The return result is an instance of the L<apiData> class.

Note: DO NOT call this function in a loop. Instead use the L<AddUsers|"AddUsers">() api function.

 Parameters:
	apiUser aUser   : The current api user's login data.
	apiUser aNewUser: The new user's data.

 Returns: apiData
	the return message from the server.
 
 Example:
	
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");
		
		my $aNewUser = new ChangeSynergy::apiUser("jsmith", "4.jsmith", "developer|ccm_admin|pt_admin",
                                                  "\\\\angler\\ccmdb\\cm_database");
		
		my $tmpstr = $csapi->AddUser($aUser, $aNewUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

#############################################################################

=item B<AddUsers>

Add a set of new users to both the LDAP server and the CM Synergy database
with the given set of CMSynergy roles. The new users can login in after this
call completes. The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser  aUser   : The current api user's login data.
	@apiUser aNewUser: A array of new user data
	scalar   iCount  : The size of the array of new users.

 Returns: apiData
	the return message from the server.
 
 Example:
	
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001","u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $i;
		my $j=100;

		my @newUsers;

		for($i=0;$i<$j;$i++)
		{
			push @newUsers, new ChangeSynergy::apiUser("ATestUser" . $i ,"ATestUser",
                                                       "developer|ccm_admin|pt_admin",
                                                       "\\\\angler\\ccmdb\\cm_database");
		}

		my $tmpstr = $csapi->AddUsers($aUser, \@newUsers, $j);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<AttributeModifyCRData>

Load the details of a Change Request into data classes in which the 
details of the Change Request can be modified. The modified data classes
can then be submitted using one of the modification api functions 
to change a Change Request.
The return result is an instance of the L<apiObjectVector> class.

Note: Current transition choices are provided with this api function call.
See L<apiTransitions> class description.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.

 Returns: apiObjectVector
	the details of a change request in data format.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->AttributeModifyCRData($aUser, "100");

		my $tmpstr = tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<AttributeModifyCRData>

Load the details of a Change Request into data classes in which the 
details of the Change Request can be modified. The modified data classes
can then be submitted using one of the modification api functions 
to change a Change Request.
The return result is an instance of the L<apiObjectVector> class.

Note: Current transition choices are provided with this api function call.
See L<apiTransitions> class description.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar  attributeName: The name of the attribute in which to look up the
	                       referenced object's current value. This value MUST
	                       be a name of a SYNERGY/Change template.

 Returns: apiObjectVector
	the details of a change request in data format.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->AttributeModifyCRData($aUser, "100", "crstatus");

		my $tmpstr = tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<AttributeModifyCRDataAllTransitions>

Load the details of a Change Request into data classes in which the 
details of the Change Request can be modified. The modified data classes
can then be submitted using one of the modification api functions 
to change a Change Request.
The return result is an instance of the L<apiObjectVector> class.
The AllTransitions function includes HIDDEN transitions.

Note: Current transition choices are provided with this api function call.
See L<apiTransitions> class description.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar  attributeName: The name of the attribute in which to look up the
	                       referenced object's current value. This value MUST
	                       be a name of a SYNERGY/Change template.

 Returns: apiObjectVector
	the details of a change request in data format.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->AttributeModifyCRDataAllTransitions($aUser, "100", "crstatus");

		my $tmpstr = tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<AttributeModifyCRDataAllTransitions>

Load the details of a Change Request into data classes in which the 
details of the Change Request can be modified. The modified data classes
can then be submitted using one of the modification api functions 
to change a Change Request.
The return result is an instance of the L<apiObjectVector> class.
The AllTransitions function includes HIDDEN transitions.

Note: Current transition choices are provided with this api function call.
See L<apiTransitions> class description.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.

 Returns: apiObjectVector
	the details of a change request in data format.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->AttributeModifyCRDataAllTransitions($aUser, "100");

		my $tmpstr = tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<AttributeModifyTaskData>

Load the details of a Task into data classes in which the details of 
the Task can be modified. The modified data classes can then be
submitted using one of the modification api functions to change a Task.
The return result is an instance of the L<apiObjectVector> class.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  taskNumber   : The Task ID to reference.
	scalar  attributeName: The name of the attribute in which to look up the
	                       referenced object's current value. This value MUST
	                       be a name of a SYNERGY/Change template.

 Returns: apiObjectVector
	the details of a task in data format
 
 Example:
 
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->AttributeModifyTaskData($aUser, "10", "status");

		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<BalanceTransactionServer>

Triggers the session balancing routine.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->BalanceTransactionServer($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<CallBsfScript>

Calls a Bean Scripting Framework (BSF) script on the server and gets its
return value. The BSF script must reside in the servers wsconfig/scripts directory.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser     : The current api user's login data.
	scalar  scriptName: The name of the script to execute on the server. Must reside in the wsconfig/script directory.
						The value will be XML encoded by this method.
	scalar  scriptData: The data that should be sent to the script as a string. Can be XML, but must be XML encoded.
						The value will be XML encoded by this method.

 Returns: apiData
	the return message from the script.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $scriptResults = $csapi->CallBsfScript($aUser, "testscript.js", "Data to the script");

		print $scriptResults->getResponseData() . "\n";
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ChangePreferenceNameForAUser>

Change the name of a user's preference for a single user.  A preference
name cannot be renamed to a preference name which already exists for 
the user. The return result is an instance of the L<apiData> class.

Note: It is not possible to change or add user profile values.  These values
are the users first names, last names, email addresses, fax numbers, telephone
numbers and addresses.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  username: The name of the user's preferences to edit.
	scalar  keyName : The name of the preference to change.
	scalar  keyValue: The new name for the preference.
	scalar  allDBs  : true or false, should the add take place for all databases
						or just the one that the current api user is logged into.

 Returns: apiData
	the return message from the server.
 
 Example:
	
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");
		
		$tmpData = $csapi->ChangePreferenceNameForAUser($aUser, "u00001", "user_cr_notes", "user_crnotes", "true");
	
		print $tmpData->getResponseData();

	};

	if ($@)
	{
		print $@;
	}

=cut

#############################################################################

=item B<ChangePreferenceNameForAllUsers>

Change the name of a user's preference for all users in the system.
A preference name cannot be renamed to a preference name which already 
exists for user. If the preference name does not exist for a user then
no changes will be made for that user.  If it does exist then the preference
name will be changed accordingly. The return result is an instance of
the L<apiData> class.

Note: It is not possible to change or add user profile values.  These values
are the users first names, last names, email addresses, fax numbers, telephone
numbers and addresses.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  keyName : The name of the preference to change.
	scalar  keyValue: The new name for the preference.
	scalar  allDBs  : true or false, should the add take place for all databases
						or just the one that the current api user is logged into.

 Returns: apiData
	the return message from the server.
 
 Example:
	
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");
		
		$tmpData = $csapi->ChangePreferenceNameForAllUsers($aUser, "user_cr_notes", "user_crnotes", "true");
	
		print $tmpData->getResponseData();

	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ChangeRequestFullName>
 
Obtains the four-part name for a Change Request.

 Parameters:
 
	apiUser aUser       : The current api user's login data.
	scalar ProblemNumber: The problem number.
 
 Returns: scalar 
	The four part name.

=cut

#############################################################################

	
=item B<ClearLog>

Clears the log file on the SYNERGY/Change server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ClearLog($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ClientAPIVersion>

Get the API version number of the client.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	The version number string.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr1 = $csapi->ClientAPIVersion($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<CopyCRData>

Load the details of a Change Request into data classes in which the details
of the Change Request can be submitted/copied. The modified data classes can
then be submitted using one of the modification api functions to change a 
Change Request. The return result is an instance of the L<apiObjectVector> class.

Note: The submit "to state" and "relation name" are provided with this api function call.
See L<apiTransitions> class description.


 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar  templateName : The name of the SYNERGY/Change template to load
	                       ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).

 Returns: apiObjectVector
	the details of a change request in data format.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->CopyCRData($aUser, "100", "COPY_child_cr2new_child");

		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<CopyTaskData>

Load the details of a Task into data classes in which the details of
the Task can be submitted/copied. The modified data classes can then
be submitted using one of the modification api functions to change a Task.
The return result is an instance of the L<apiObjectVector> class.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  taskNumber  : The Task ID to reference.
	scalar  templateName: The name of the SYNERGY/Change template to load 
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).

 Returns: apiObjectVector
	the details of a task in data format.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->CopyTaskData($aUser, "12", "CreateTask");

		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<CreateAttachmentObject>

Create an attachment file object on the SYNERGY/Change server and relates it to a CR.
The return result is an instance of the L<apiData> class. 


 Parameters:
	apiUser aUser         : The current api user's login data.
	scalar  problemNumber : The ProblemNumber/CR ID to relate the file to.
	scalar  relation      : The relation name to use when relating the object to the CR.
	scalar  attachmentName: The file name for this object.
	scalar  webType       : Carriage return sequence on client.
	                              CRLF:   Windows client text file.
	                              LF:     Unix client text file.
	                              BINARY: File is binary.
	scalar  comment       : The comments for the object to update.
	scalar  type          : Reserved for future use.
	scalar  isBinary      : A flag to specify that the file is a binary file.
	scalar  buffer        : A buffer of the data.
	scalar  size          : The size of the buffer.

 Returns: apiData
	the return message from the server.

 Example:

	my $csapi  = new ChangeSynergy::csapi();
	my $buf    = "";
	my $buffer = "";
	my $size   = "";

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		open(INPUTFILE, "output.doc") or die "Could not open up the file";

		while($buf = readline *INPUTFILE)
		{
			$buffer .= $buf;
		}

		close(INPUTFILE);
	
		$size = -s "my.doc";
    	
		my $data = $csapi->CreateAttachmentObject($aUser, "1", "attachment", "output",
											   "BINARY", "The output", "", "true", $buffer, $size);
		print $data->getResponseData();
	};
    
	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<CreateCSObject>

Creates a component version entity with model "model".
See CreateNewCV for a full description.
 
The cvtype, and name arguments are used to set the values of the full name 
attributes of the new entity. The creation will fail if the full name is not
unique among all component versions in the CMSynergy database.

CVs may contain names with the alpha-numerics and !&^~@*_.+: However, it is still
possible for a particular model to impose more constrained naming rules.

Note: If "cvtype" is a empty string, then the type will be "cs_object".

Note: "cvtype" must be the name of a component version type component 
      version in the model assembly model.

 Note: If "State" is a empty string then the status will default to "cs_public".

 Note: Default state change from (ac_def -> cs_public).
       No transitions are available in default state!

The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  cvtype  : The cvtype value of the desired four part compver name.
	scalar  name    : The name value of the desired four part compver name.
	scalar  state   : The status (state) value to be automatically transitioned to.

 Returns: apiData
	The return message from the server.
	Use the getResponseData() method to retrieve the compver id.
	The string value will be, ex: "CV cvid = 5_digit_integer_value_of_compver"
	
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->CreateCSObject($aUser, "admin", "special","");

		print $tmp->getResponseData(); #ex: "CV cvid = 12345"

		#Note: Result will be like: "CV cvid = 5_digit_integer_value_of_compver".
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<CreateDefaultCSObject>

Creates a component version entity with model "model".
See CreateNewCV for a full description.

The name argument is used to set the value of the full name attributes of the
new entity. The creation will fail if the full name is not unique among all
component versions in the CMSynergy database.
 
CVs may contain names with the alpha-numerics and !&^~@*_.+: However, it is still
possible for a particular model to impose more constrained naming rules.  
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser  : The current api user's login data.
	scalar  name   : The name value of the desired four part compver name.

 Returns: apiData
	The return message from the server.
	Use the getResponseData() method to retrieve the compver id.
	The string value will be, ex: "CV cvid = 5_digit_integer_value_of_compver"
	
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->CreateDefaultCSObject($aUser, "special");

		print $tmp->getResponseData(); #ex: "CV cvid = 12345"

		#Note: Result will be like: "CV cvid = 5_digit_integer_value_of_compver".
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<CreateIndex>

Create the search index on the SYNERGY/Change Server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->CreateIndex($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<CreateMiscObject>

Create a misc object. The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  objectString: The object identifier to be created.
 
 Returns: apiData
	CVID of the new object.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->CreateMiscObject($aUser, "DOORS_ID_400");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<CreateNewCV>

WARNING:
This method is not intended for general use. Users of this method must be
very familiar with ACcent programming. Use the general "CreateCSObject"
or "CreateDefaultCSObject" api methods.

Creates a component version entity with model "model".

[subsys/cvtype/name/version]
ex: "1/admin/cs/1"

The subsys, cvtype, name, and version arguments are used to set the values of the
full name attributes of the new entity. The creation will fail if the full name is
not unique among all component versions in the CMSynergy database.

CVs may contain names with the alpha-numerics and !&^~@*_.+: However, it is still
possible for a particular model to impose more constrained naming rules.
 
Note: If "version" is a empty string, then the version will be "1".

Note: If "cvtype" is a empty string, then the type will be "cs_object".

Note: "cvtype" must be the name of a component version type component 
       version in the model assembly model.

Predefined cvtypes on the default model:
           cs_object,admin,ascii,asm0,baseline,binary,bitmap,c++,class,csrc,
           css,dir,dtd,executable,folder,folder_temp,gif,group,html,
           incl,jar,java,jpeg,library,lsrc,makefile,misc,perl,problem,
           project,recon_temp,releasedef,relocatable_obj,shared_library,
           shsrc,symlink,task,tset,xml,ysrc

Note: Do not add the DBID and DCM delimiter to the "subsys". These values will be
automatically added if DCM/DCS is initialized. If the DBID and DCM delimiter are added
then a subsystem of that looks like foo#foo#1 would be created instead of foo#1.

Note: If "subsys" is a empty string, then the instance_number will be calculated.
      If DCM/DCS is initialized, the DCM database id and DCM delimiter are
      used in addition to the "subsys" or calculated instance. 

      DCM initialized:
         ex: db63#1/cs_object/your_name/1
 
      Not DCM initialized:
         ex: 1/cs_object/your_name/1
 
The following attributes of the new entity may/will be created and given values:

 create_time  : time    : Current time.
 cvtype       : string  : Argument cvtype.
 is_asm       : boolean : Component version type's "is_asm" attribute value.
 is_model     : boolean : Component version type's "is_model" attribute value.
 local_bgraph : boolean : FALSE.
 modify_time  : time    : Current time.
 name         : string  : Argument name.
 owner        : string  : Current user.
 status       : string  : Component version type's "dflt_status" attribute value.
 subsystem    : string  : Argument subsys.
 version      : string  : Argument version.
 
Note: If "State" is a empty string then the status will default to "cs_public".

Note: Default state change from (ac_def -> cs_public).
      No transitions are available in default state!

Default security is based on CHANGE_STATE = "cs_public"

			  *** SYSTEM PREDEFINED STATES ***
 state working            = private + read + eval;
 state visible            = private + read + eval + bind;
 state working_folder     = private + read + eval + user1;
 state checkpoint         = private + read + eval + user0;

 state readonly           = static + read + eval;
 state cs_admin           = static + read + user9;
 state published_baseline = static + read + eval + user7;
 state released           = static + read + eval + derive + bind;
 state readonly_folder    = static + read + eval + derive + user0;
 state rejected           = static + read + eval + derive + bind + user3;
 state test               = static + read + eval + derive + bind + user2;
 state sqa                = static + read + eval + derive + bind + user0;
 state integrate          = static + read + eval + derive + bind + user1;

 state forwarded          = read + write;
 state task_deferred      = read + write + user0;
 state registered         = read + write + user1;
 state task_assigned      = read + write + user2;
 state completed          = read + write + user3;
 state deleted            = read + write + user4;
 state excluded           = read + write + user5;
 state task_automatic     = read + write + user6;
 state public             = read + eval  + bind   + write;
 state crbase             = read + write + eval   + user1;
 state entered            = read + write + eval   + user2;
 state deferred           = read + write + eval   + user3;
 state concluded          = read + write + eval   + user4;
 state duplicate          = read + write + user1  + user2;
 state working_recon_temp = read + eval  + write  + user5;
 state static_recon_temp  = read + eval  + static + user5;
 state prep_baseline      = read + eval  + write  + user7;
 state shared_folder      = read + eval  + derive + write;
 state shared             = read + eval  + derive + bind  + write;
 state admin              = read + eval  + bind   + write + user0;
 state release_admin      = read + eval  + write  + user0 + user1;
 state cs_public          = read + eval  + bind   + write + user8;
 state in_review          = read + write + eval   + bind  + user1;
 state assigned           = read + write + eval   + bind  + user2;
 state probreject         = read + write + eval   + bind  + user3;
 state resolved           = read + write + eval   + bind  + user4;
 state prep_folder        = read + eval  + derive + write + user1;
 state prep               = read + eval  + derive + bind  + write + user0;
 state dcm_admin          = read + eval  + bind   + write + user0 + user1;

The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  subsys  : The subsys value of the desired four part compver name.
	scalar  cvtype  : The cvtype value of the desired four part compver name.
	scalar  name    : The name value of the desired four part compver name.
	scalar  version : The version value of the desired four part compver name.
	scalar  state   : The status (state) value to be automatically transitioned to.

 Returns: apiData
	The return message from the server.
	Use the getResponseData() method to retrieve the compver id.
	The string value will be, ex: "CV cvid = 5_digit_integer_value_of_compver"
	
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->CreateNewCV($aUser, "", "admin", "special", "1", "");

		print $tmp->getResponseData(); #ex: "CV cvid = 12345"

		#Note: Result will be like: "CV cvid = 5_digit_integer_value_of_compver".
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<CreateObjectAttributes>

Creates new attribute(s) of compver with name "your name value" and attribute type "your type value."
"type" must be a member of compver's model assembly. The initial value given to the attribute 
must be provided. This operation also updates the compver's modify_time attribute. The return
result is an instance of the L<apiData> class.

 Parameters:
	apiUser         aUser       : The current api user's login data.
	scalar          cvidList    : A "|" pipe delimited list of cvids to be affected, or a single cvid.
	apiObjectVector attrData    : The data to be processed by the api function.
 
 Returns: apiData
	The return message from the server.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $attrData = new ChangeSynergy::apiObjectVector();

		my $objData = new ChangeSynergy::apiObjectData();
		$objData->setName("attribute_a");
		$objData->setType("text");
		$objData->setValue("Linux");
		$attrData->addDataObject($objData);

		my $objData = new ChangeSynergy::apiObjectData();
		$objData->setName("attribute_b");
		$objData->setType("boolean");
		$objData->setValue("true");
		$attrData->addDataObject($objData);

		my $objData = new ChangeSynergy::apiObjectData();
		$objData->setName("attribute_c");
		$objData->setType("integer");
		$objData->setValue("777");
		$attrData->addDataObject($objData);

		my $tmp = $csapi->CreateObjectAttributes($aUser, "10156|10157|10158|10159|10160", $attrData)

		print $tmp->getResponseData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<CreateRelation>

Create a relation between two CM Synergy objects.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser              : The current api user's login data.
	scalar  bothWayRelationship: Create a relationship in both directions, [true|false].
	scalar  fromObject         : The object from which the relation is created.
	scalar  toObject           : The object to which the relation is applied.
	scalar  relationName       : A valid CMSynergy/SYNERGY/Change relation name.
	scalar  relationType       : The relation type, see below.

 Valid Relation Types (Constants defiend in Globals.pm):
        CCM_PROBLEM_PROBLEM  // Create a Change Request to Change Request relation
        CCM_PROBLEM_TASK     // Create a Change Request to Task relation
        CCM_PROBLEM_OBJECT   // Create a Change Request to Object relation
        CCM_TASK_PROBLEM     // Create a Task to Change Request relation
        CCM_TASK_TASK        // Create a Task to Task relation
        CCM_TASK_OBJECT      // Create a Task to Object relation
        CCM_OBJECT_PROBLEM   // Create a Object to Change Request relation
        CCM_OBJECT_TASK      // Create a Object to Task relation
        CCM_OBJECT_OBJECT    // Create a Object to Object relation
        
        Example usage:
          my $globals = new ChangeSynergy::Globals();
          my $relationType = $globals->{CCM_PROBLEM_PROBLEM};

 Returns: apiData
	results on if the creation was successful.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $globals = new ChangeSynergy::Globals();

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->CreateRelation($aUser, "FALSE", "400", "1355", "my_copy", 
                                            $globals->{CCM_PROBLEM_PROBLEM});
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<CreateUserSecurityData>

Create user security files on the server.

 Parameters:
 
	apiUser aUser: The current api user's login data.
 
 Returns: scalar
	A return message.


 Example:

	my $csapi = new ChangeSynergy::csapi();
	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->CreateUserSecurityData($aUser);
	}

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<CSHostName>

Get the configured host name for the ChangeSynergy server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the host name string.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->CSHostName($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<DatabaseGetObject>

Copy a database object into a new BYTE array.
The return result is an instance of the L<apiData> class. 

 Parameters:
	apiUser aUser: The current api user's login data.
	scalar  Cvid : The cvid of the source object to retrieve.

 Returns: apiData
	the byte data from the server
	
 Example:
 
 	$csapi->setUpConnection("http", "angler", 8600);
 	
 	eval
 	{
 		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");
 		my $data  = $csapi->DatabaseGetObject($aUser, "11023");

		open(OUTPUT, ">file.txt");
		print(OUTPUT $data->getResponseByteData());
		close(OUTPUT);
 	};
 	
 	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<DatabaseSetObject>

Update a file object on the SYNERGY/Change server.
The return result is an instance of the L<apiData> class. 

 Parameters:
	apiUser aUser  : The current api user's login data.
	scalar  cvid   : The cvid of the source object to update.
	scalar  comment: The comments for the object to update.
	scalar  buffer : The BYTE data to set on the server.
	scalar  size   : The size of the BYTE data.

 Returns: apiData
	the return message from the server.
	
 Example:
 
 	$csapi->setUpConnection("http", "angler", 8600);

 	my $buf    = "";
	my $buffer = "";
	my $size   = "";
 	
	eval
	{
		my $aUser      = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");
 		
		open(INPUTFILE, "input.txt") or die "Could not open up the file";

		while($buf = readline *INPUTFILE)
		{
			$buffer .= $buf;
		}

		close(INPUTFILE);
    
		$size = -s "input.txt";
    	
		my $data = $csapi->DatabaseSetObject($aUser, "10341", "new comment", $buffer, $size);
	};
 	
	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<DeleteAPreferenceForAUser>

Delete a preference for a user in the system.  Warning - this 
permanently deletes a single preferences for a user; there is
no recovery option. The return result is an instance of the L<apiData>
class.

Note: It is not possible to delete user profile values.  These values
are the users first names, last names, email addresses, fax numbers, telephone
numbers and addresses.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  username: The name of the user's preferences to delete.
	scalar  keyname : The name of the preference to delete.
	scalar  allDBs  : true or false, should the add take place for all databases
						or just the one that the current api user is logged into.

 Returns: apiData
	the return message from the server.
 
 Example:
	
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");
		
		$tmpData = $csapi->DeleteAPreferenceForAUser($aUser, "u00001", "user_fontsize", "true");
	
		print $tmpData->getResponseData();

	};

	if ($@)
	{
		print $@;
	}

=cut

#############################################################################


=item B<DeleteAPreferenceForAllUsers>

Delete a preference for all users in the system.  Warning - this permanently 
this deletes a single preferences for ALL users; there is no recovery 
option. The return result is an instance of the L<apiData> class.

Note: It is not possible to delete user profile values.  These values
are the users first names, last names, email addresses, fax numbers, telephone
numbers and addresses.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  keyname : The name of the preference to delete.
	scalar  allDBs  : true or false, should the add take place for all databases
						or just the one that the current api user is logged into.

 Returns: apiData
	the return message from the server.
 
 Example:
	
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");
		
		$tmpData = $csapi->DeleteAPreferenceForAllUsers($aUser, "user_fontsize" "true");

		print $tmpData->getResponseData();

	};

	if ($@)
	{
		print $@;
	}

=cut

#############################################################################

=item B<DeleteAUsersPreferences>

Delete the preference object for a single user in the system.  Warning -
this permanently deletes ALL preferences for a single user; there is no recovery 
option. The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  username: The name of the user's preferences to delete

 Returns: apiData
	the return message from the server.
 
 Example:
	
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");
		
		$tmpData = $csapi->DeleteAUsersPreferences($aUser, "u00001");
	
		print $tmpData->getResponseData();

	};

	if ($@)
	{
		print $@;
	}

=cut

#############################################################################


=item B<DeleteAllUserPreferences>

Delete the preference object for all users in the system.  Warning - this
permanently deletes ALL preferences for ALL users;  there is no recovery
option. The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser   : The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:
	
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");
		
		$tmpData = $csapi->DeleteAllUserPreferences($aUser);
	
		print $tmpData->getResponseData();

	};

	if ($@)
	{
		print $@;
	}

=cut

#############################################################################

=item B<DeleteChangeRequest>

Delete a Change Request. The return result is an instance of the L<apiData> class. 

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The problem number to delete.

 Returns: apiData
	The delete status message.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->DeleteChangeRequest($aUser, "10");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<DeleteCV>

Deletes compver and all subordinate objects and attributes from the database. 
The subordinate objects include collectors, processors, connectors, bindings
(in the case of an assembly), and binding sites. The entity will not be 
deleted if any of the following conditions are true:

         > compver is a member of an existing assembly.
         > compver is a model assembly and component versions with it as model exist.
         > compver is an attribute, binding site, component version, or product type
               component version and instances of it currently exist.
         > compver is an attribute, binding site, component version, or product type
               component version and is also the super_type of another existing type
               component version.

The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser : The current api user's login data.
	scalar  cvid  : The cvid of the compver to delete.
 
 Returns: apiData
	The return message from the server.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->DeleteCV($aUser,"10159");

		print $tmp->getResponseData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<DeleteNewCV>

Deletes compver and all subordinate objects and attributes from the database. 
The subordinate objects include collectors, processors, connectors, bindings
(in the case of an assembly), and binding sites. The entity will not be 
deleted if any of the following conditions are true:

         > compver is a member of an existing assembly.
         > compver is a model assembly and component versions with it as model exist.
         > compver is an attribute, binding site, component version, or product type
               component version and instances of it currently exist.
         > compver is an attribute, binding site, component version, or product type
               component version and is also the super_type of another existing type
               component version.

The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  Subsys  : The subsys value of the desired four part compver name.
	scalar  cvtype  : The cvtype value of the desired four part compver name.
	scalar  name    : The name value of the desired four part compver name.
	scalar  version : The version value of the desired four part compver name.
 
 Returns: apiData
	The return message from the server.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->DeleteNewCV($aUser, "3", "admin", "special", "1");

		print $tmp->getResponseData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<DeleteObjectAttributes>

Deletes existing attribute(s) of compver with name "your name value." This operation
also updates the compver's modify_time attribute. The return result is an instance of
the L<apiData> class.

 Parameters:
	apiUser         aUser       : The current api user's login data.
	scalar          cvidList    : A "|" pipe delimited list of cvids to be affected, or a single cvid.
	apiObjectVector attrData    : The data to be processed by the api function.
 
 Returns: apiData
	The return message from the server.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $attrData = new ChangeSynergy::apiObjectVector();

		my $objData = new ChangeSynergy::apiObjectData();
		$objData->setName("attribute_a");
		$attrData->addDataObject($objData);

		my $objData = new ChangeSynergy::apiObjectData();
		$objData->setName("attribute_b");
		$attrData->addDataObject($objData);

		my $objData = new ChangeSynergy::apiObjectData();
		$objData->setName("attribute_c");
		$attrData->addDataObject($objData);

		my $tmp = $csapi->DeleteObjectAttributes($aUser, "10156|10157|10158|10159|10160", $attrData)

		print $tmp->getResponseData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<DeleteRelation>

Delete a relation between two CM Synergy objects.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser              : The current api user's login data.
	scalar  bothWayRelationship: Create a relationship in both directions, [true|false].
	scalar  fromObject         : The object from which the relation is created.
	scalar  toObject           : The object to which the relation is applied.
	scalar  relationName       : A valid CMSynergy/SYNERGY/Change relation name.
	scalar  relationType       : The relation type, see below.

 Valid Relation Types (Constants defiend in Globals.pm):
        CCM_PROBLEM_PROBLEM	// Create a Change Request to Change Request relation
        CCM_PROBLEM_TASK		// Create a Change Request to Task relation
        CCM_PROBLEM_OBJECT		// Create a Change Request to Object relation
        CCM_TASK_PROBLEM		// Create a Task to Change Request relation
        CCM_TASK_TASK		// Create a Task to Task relation
        CCM_TASK_OBJECT		// Create a Task to Object relation
        CCM_OBJECT_PROBLEM		// Create a Object to Change Request relation
        CCM_OBJECT_TASK		// Create a Object to Task relation
        CCM_OBJECT_OBJECT		// Create a Object to Object relation
        
        Example usage:
          my $globals = new ChangeSynergy::Globals();
          my $relationType = $globals->{CCM_PROBLEM_PROBLEM};

 Returns: apiData
	results on if the deletion was successful.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $globals = new ChangeSynergy::Globals();

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->DeleteRelation($aUser, "FALSE", "400", "1355", "my_copy", 
                                            $globals->{CCM_PROBLEM_PROBLEM});
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<DeleteTask>

Delete a Task. The return result is an instance of the L<apiData> class. 

 Parameters:
	apiUser aUser     : The current api user's login data.
	scalar  taskNumber: The task number to delete.

 Returns: apiData
	The delete status message.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->DeleteTask($aUser, "1");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<DisableDatabase>

Disable a SYNERGY/Change database on the SYNERGY/Change server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  database: The database to disable.

 Returns: apiData
	the return message from the server.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->DisableDatabase($aUser, "\\\\angler\\ccmdb\\cm_database");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<DisableHost>

Disable a SYNERGY/Change host on the SYNERGY/Change server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.
	scalar  host : The host to disable.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");


		my $tmpstr = $csapi->DisableHost($aUser, "cm_host");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<DisableIndexing>

Force indexing to stop on the SYNERGY/Change Server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->DisableIndexing($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<DumpAUsersPreferences>

Get the entire contents of the user's preferences returned as a string.
This string contains the name and value for everything found in a user's
preference object.  This is helpful for debugging purposes and ensuring
the desired changes have taken effect.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  username: The users preference data to get.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->DumpAUsersPreferences($aUser, "u00001");
		print $tmpstr->getResponseData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<EnableDatabase>

Enable a SYNERGY/Change database on the SYNERGY/Change server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  database: The database to enable.

 Returns: apiData
	the return message from the server.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->EnableDatabase($aUser, "\\\\angler\\ccmdb\\cm_database");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<EnableHost>

Enable a SYNERGY/Change host on the SYNERGY/Change server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.
	scalar  host : The host to enable.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");


		my $tmpstr = $csapi->EnableHost($aUser, "cm_host");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<EnableIndexing>

Allow indexing to resume on the SYNERGY/Change Server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->EnableIndexing($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetAttributes>

Gets all SYNERGY/Change attributes defined on the server.
A SYNERGY/Change attribute is:

	[CCM_ATTRIBUTE]
		[NAME]
			The SYNERGY/Change Attribute name.
		[/NAME]
		[TYPE]
			The Web visualization data type, 
			available types are: CCM_STRING, CCM_TEXT, CCM_LISTBOX,
			and CCM_VALUELISTBOX.
		[/TYPE]
		[ROLE NAME]
			Optional role based aliases.
			There can be as many role options as there are defined web roles.
			Where "ROLE NAME" and "/ROLE NAME" are the literal role name.
		[/ROLE NAME]...
		[ALIAS]
			The default alias value for the attribute. This value is returned
			if role options are not used or if the users role is not specified.

			The [ALIAS] tag set defines the default, if no [ALIAS] tag exists
			the [NAME] is returned.
		[/ALIAS]
	[/CCM_ATTRIBUTE]

The [NAME] is identified through the getName() method.
The [TYPE] is identified through the getType() method.
The [ALIAS] is identified through the getLabel() method.
The [ROLE NAME] option is not available through the api.

The return result is an instance of the L<apiObjectVector> class.

 Parameters:
	apiUser aUser: The current api user's login data.
 
 Returns: apiObjectVector
	All of the SYNERGY/Change attributes defined on the server.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $attrs = $csapi->GetAttributes($aUser);

		my $i;
		my $j = $attrs->getDataSize();

		for($i=0; $i < $j; $i++)
		{
			print $attrs->getDataObject($i)->getName() . "\n";  #[CCM_ATTRIBUTE][NAME] 
			print $attrs->getDataObject($i)->getType() . "\n";  #[CCM_ATTRIBUTE][TYPE]
			print $attrs->getDataObject($i)->getLabel() . "\n"; #[CCM_ATTRIBUTE][ALIAS]
		}
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetCRData>

Load the details of a Change Request into data classes in which the 
details of the Change Request can be modified. The modified data classes
can then be submitted using one of the modification api functions 
to change a Change Request. The return result is an instance of
the L<apiObjectVector> class.

Note: Current transition choices are provided with this api function call.
See L<apiTransitions> class description.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar  attributeList: A delimited list of attributes. 
	                       [attribute_name|attribute_name|attribute_name|...]

 Returns: apiObjectVector
	the details of a change request in data format.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->GetCRData($aUser, "100", ""problem_synopsis|problem_description");

		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetCRDataAllTransitions>

Load the details of a Change Request into data classes in which the 
details of the Change Request can be modified. The modified data classes
can then be submitted using one of the modification api functions 
to change a Change Request. The return result is an instance of
the L<apiObjectVector> class.
The AllTransitions function includes HIDDEN transitions.

Note: Current transition choices are provided with this api function call.
See L<apiTransitions> class description.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar  attributeList: A delimited list of attributes. 
	                       [attribute_name|attribute_name|attribute_name|...]

 Returns: apiObjectVector
	the details of a change request in data format.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->GetCRDataAllTransitions($aUser, "100", ""problem_synopsis|problem_description");

		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetCV>

Obtains the four part name for a compver. 
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.
	scalar  cvid : The cvid of the compver to get.

 Returns: apiData
	Four part name: [subsys/cvtype/name/version], ex: "1/admin/cs/1"
	
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->GetCV($aUser,"10159");

		print $tmp->getResponseData(); #ex: "3/admin/special/1"

		#Note: Result will be a four part name like: "[subsys/cvtype/name/version]", in string format.
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetDatabases>

Get the list of SYNERGY/Change databases from the SYNERGY/Change server.
The return result is an instance of the L<apiListObject> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiListObject
	a list of the all the databases on the SYNERGY/Change server.
	
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->GetDatabases($aUser);

		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetDataListBox>

Get the contents of a DataListbox.
The return result is an instance of the L<apiListObject> class.

 Parameters:
	apiUser aUser     : The current api user's login data.
	scalar  listObject: The DataListbox to obtain.

 Returns: apiListObject
	the contents of the DataListbox.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $list = $csapi->GetDataListBox($aUser, "CRQUERYREPORTPREDEFINED");

		for(my $i=0; $i < $list->getListboxSize(); $i++)
		{
			my $label = $list->getLabel($i);
			my $value = $list->getValue($i);

			print "List label $i: " . $label . "\n";
			print "List value $i: " . $value . "\n";
		}
	};

	if ($@)
	{
		print $@;
	}

=cut

#############################################################################

=item B<GetDataListBox>

Get the contents of a DataListbox.
The return result is an instance of the L<apiListObject> class.

 Parameters:
	apiUser aUser     : The current api user's login data.
	scalar  listObject: The DataListbox to obtain.
	scalar  configType: The config entry to search for the list in.  
	
	Valid Config Types: These are defined in the Globals class.
        $self->{ALL}       		// User, Shared and System. Returns the first one found.
        $self->{USER_PROFILE}	// A single users profile data.
        $self->{SHARED_PROFILE} // The shared profile data.
	    $self->{SYSTEM_CONFIG}  // The system config data.

 Returns: apiListObject
	the contents of the DataListbox.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $globals = new ChangeSynergy::Globals();

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $list = $csapi->GetDataListBox($aUser, "CRQUERYREPORTUSERDEFINED", $globals->{USER_PROFILE});

		for(my $i=0; $i < $list->getListboxSize(); $i++)
		{
			my $label = $list->getLabel($i);
			my $value = $list->getValue($i);

			print "List label $i: " . $label . "\n";
			print "List value $i: " . $value . "\n";
		}
	};

	if ($@)
	{
		print $@;
	}

=cut

#############################################################################

=item B<GetDOORSAttribute>

Get a DOORS attribute tag value from a DOORS attachment object.

 Parameters:
	apiUser aUser          : A pointer to the current api user's login data.
	scalar  Cvid           : The cvid of the source object to retrieve.
	scalar  attributeValue : The DOORS_ATTR:NAME value of the desired DOORS attribute.
	scalar  attributeTag   : The name of the tag to get information from 
	                         [NAME|TYPE|RANGE|VALUE|DEFAULT_AR|USER|GROUP].
	scalar  objectType     : The xml root tag [DYNAMIC_ATTRS_ORIG|DYNAMIC_ATTRS_NEW].
	scalar  charSet        : The character set to use. ie: "UTF-16LE", "iso-8859-1"

 Returns: apiData
	the return message from the server.
 
 Example:
	
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->GetDOORSAttribute($aUser, "10126", "the name", "VALUE", "DYNAMIC_ATTRS_ORIG", "UTF-16LE");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetHosts>

Get the list of SYNERGY/Change hosts.
The return result is an instance of the L<apiListObject> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiListObject
	a list of all the hosts on the SYNERGY/Change server
 
 Example:
 
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->GetHosts($aUser);

		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetList>

Get the contents of a List.
The return result is an instance of the L<apiListObject> class.

 Parameters:
	apiUser aUser     : The current api user's login data.
	scalar  listObject: The List to obtain.

 Returns: apiListObject
	the contents of the List.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $list = $csapi->GetList($aUser, "CRQueryReportPreDefined");

		for(my $i=0; $i < $list->getListboxSize(); $i++)
		{
			my $label = $list->getLabel($i);
			my $value = $list->getValue($i);

			print "List label $i: " . $label . "\n";
			print "List value $i: " . $value . "\n";
		}
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetList>

Get the contents of a List.
The return result is an instance of the L<apiListObject> class.

 Parameters:
	apiUser aUser     : The current api user's login data.
	scalar  listObject: The List to obtain.
	scalar  configType: The config entry to search for the list in.  
	
	Valid Config Types: These are defined in the Globals class.
        $self->{ALL}       		// User, Shared and System. Returns the first one found.
        $self->{USER_PROFILE}	// A single users profile data.
        $self->{SHARED_PROFILE} // The shared profile data.
	    $self->{SYSTEM_CONFIG}  // The system config data.

 Returns: apiListObject
	the contents of the List.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $globals = new ChangeSynergy::Globals();

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $list  = $csapi->GetList($aUser, "CRQUERYUSERDEFINED", $globals->{USER_PROFILE});

		for(my $i=0; $i < $list->getListboxSize(); $i++)
		{
			my $label = $list->getLabel($i);
			my $value = $list->getValue($i);

			print "List label $i: " . $label . "\n";
			print "List value $i: " . $value . "\n";
		}
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetListBox>

Get the contents of a Listbox.
The return result is an instance of the L<apiListObject> class.

 Parameters:
	apiUser aUser     : The current api user's login data.
	scalar  listObject: The Listbox to obtain.

 Returns: apiListObject
	the contents of the Listbox.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $list  = $csapi->GetListBox($aUser, "severity");

		for(my $i=0; $i < $list->getListboxSize(); $i++)
		{
			my $label = $list->getLabel($i);
			my $value = $list->getValue($i);

			print "Listbox label $i: " . $label . "\n";
			print "Listbox value $i: " . $value . "\n";
		}
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetListBox>

Get the contents of a Listbox.
The return result is an instance of the L<apiListObject> class.

 Parameters:
	apiUser aUser     : The current api user's login data.
	scalar  listObject: The Listbox to obtain.
	scalar  configType: The config entry to search for the listbox in.  
	
	Valid Config Types: These are defined in the Globals class.
        $self->{ALL}       		// User, Shared and System. Returns the first one found.
        $self->{USER_PROFILE}	// A single users profile data.
        $self->{SHARED_PROFILE} // The shared profile data.
	    $self->{SYSTEM_CONFIG}  // The system config data.

 Returns: apiListObject
	the contents of the Listbox.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $globals = new ChangeSynergy::Globals();

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->GetListBox($aUser, "severity", $globals->{USER_PROFILE});

		for(my $i=0; $i < $list->getListboxSize(); $i++)
		{
			my $label = $list->getLabel($i);
			my $value = $list->getValue($i);

			print "Listbox label $i: " . $label . "\n";
			print "Listbox value $i: " . $value . "\n";
		}
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetNewCV>

Given a four part name, returns the cvid of the compver. 
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  subsys  : The subsys value of the desired four part compver name.
	scalar  cvtype  : The cvtype value of the desired four part compver name.
	scalar  name    : The name value of the desired four part compver name.
	scalar  version : The version value of the desired four part compver name.

 Returns: apiData
	Cvid string value: "CV cvid = 5_digit_integer_value_of_compver", ex: "CV cvid = 12345"
	
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->GetNewCV($aUser, "3", "admin", "special", "1");

		print $tmp->getResponseData(); #ex: "CV cvid = 12345"

		#Note: Result will be like: "CV cvid = 5_digit_integer_value_of_compver", in string format.
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetObjectData>

Load the details of a compver into data classes in which the details of the
compver can be modified or displayed. The modified data classes can be
submitted using one of the modification api functions.  The return
result is an instance of the L<apiObjectVector> class.

 Parameters:
	apiUser aUser     : The current api user's login data.
	scalar  cvid      : The cvid of a compver.
	scalar  AttrList  : A delimited list of attributes. [attribute_name|attribute_name|attribute_name|...]

Returns: apiObjectVector
	The contents of the attributes requested.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $objVector = $csapi->GetObjectData($aUser, $cv1, "create_time|cvtype|is_asm|is_model|is_versioned|modify_time|name|owner|status|subsystem|version");

		my $i;
		my $j = $objVector->getDataSize();

		for($i=0; $i < $j; $i++)
		{
			print "Name : " . $objVector->getDataObject($i)->getName() . "\n";
			print "Value: " . $objVector->getDataObject($i)->getValue() . "\n";
		}
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetReport>

Get the contents of a Report.
The return result is an instance of the L<apiListObject> class.

 Parameters:
	apiUser aUser     : The current api user's login data.
	scalar  listObject: The Report to obtain.

 Returns: apiListObject
	the contents of the Report.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $report = $csapi->GetReport($aUser, "Basic Summary");

		print "getName        : " . $report->getName()        . "\n";
		print "getExportForm  : " . $report->getExportForm () . "\n";
		print "getQueryName   : " . $report->getQueryName()   . "\n";
		print "getQueryString : " . $report->getQueryString() . "\n";
		print "getDateLastRun : " . $report->getDateLastRun() . "\n";
	
		for(my $i = 0; $i < $report->getSubreportSize(); $i++)
		{
			print "   Subreport $i \n";
			print "		getSubreportName    : "  . $report->getSubreportName($i)     . "\n";
			print "		getSubreportRelation: "  . $report->getSubreportRelation($i) . "\n";
			print "		getSubreportType    : "  . $report->getSubreportType($i)     . "\n";
		}
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetReport>

Get the contents of a Report.
The return result is an instance of the L<apiListObject> class.

 Parameters:
	apiUser aUser     : The current api user's login data.
	scalar  listObject: The Report to obtain.
	scalar  configType: The config entry to search for the report in.  
	
	Valid Config Types: These are defined in the Globals class.
        $self->{ALL}       		// User, Shared and System. Returns the first one found.
        $self->{USER_PROFILE}	// A single users profile data.
        $self->{SHARED_PROFILE} // The shared profile data.
	    $self->{SYSTEM_CONFIG}  // The system config data.

 Returns: apiListObject
	the contents of the Report.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $globals = new ChangeSynergy::Globals();

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $report = $csapi->GetReport($aUser, "Test Format", $globals->{USER_PROFILE});

		print "getName        : " . $report->getName()        . "\n";
		print "getExportForm  : " . $report->getExportForm () . "\n";
		print "getQueryName   : " . $report->getQueryName()   . "\n";
		print "getQueryString : " . $report->getQueryString() . "\n";
		print "getDateLastRun : " . $report->getDateLastRun() . "\n";
	
		for(my $i = 0; $i < $report->getSubreportSize(); $i++)
		{
			print "   Subreport $i \n";
			print "		getSubreportName    : "  . $report->getSubreportName($i)     . "\n";
			print "		getSubreportRelation: "  . $report->getSubreportRelation($i) . "\n";
			print "		getSubreportType    : "  . $report->getSubreportType($i)     . "\n";
		}
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetTaskData>

Load the details of a Task into data classes in which the details of
the Task can be modified. The modified data classes can then be
submitted using one of the modification api functions to change a Task.
The return result is an instance of the L<apiObjectVector> class.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  taskNumber   : The Task ID to reference.
	scalar  attributeList: A delimited list of attributes. 
	                       [attribute_name|attribute_name|attribute_name|...]

 Returns: apiObjectVector
	the details of a task in data format.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->GetTaskData($aUser, "10", "task_synopsis|task_description|priority");

		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetQuery>

Get the contents of a Query.
The return result is an instance of the L<apiListObject> class.

 Parameters:
	apiUser aUser     : The current api user's login data.
	scalar  listObject: The Query to obtain.

 Returns: apiListObject
	the contents of the Query.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $query = $csapi->GetQuery($aUser, "All CRs");

		print "getName       : " . $query->getName() . "\n";
		print "getQueryString: " . $query->getQueryString() . "\n";
		print "getDateLastRun: " . $query->getDateLastRun() . "\n";
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetQuery>

Get the contents of a Query.
The return result is an instance of the L<apiListObject> class.

 Parameters:
	apiUser aUser     : The current api user's login data.
	scalar  listObject: The Query to obtain.
	scalar  configType: The config entry to search for the query in.  
	
	Valid Config Types: These are defined in the Globals class.
        $self->{ALL}       		// User, Shared and System. Returns the first one found.
        $self->{USER_PROFILE}	// A single users profile data.
        $self->{SHARED_PROFILE} // The shared profile data.
	    $self->{SYSTEM_CONFIG}  // The system config data.

 Returns: apiListObject
	the contents of the Query.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $globals = new ChangeSynergy::Globals();

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $query = $csapi->GetQuery($aUser, "Test Query", $globals->{USER_PROFILE});

		print "getName       : " . $query->getName() . "\n";
		print "getQueryString: " . $query->getQueryString() . "\n";
		print "getDateLastRun: " . $query->getDateLastRun() . "\n";

	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################


=item B<GetUserPreference>

Get a user preference or profile value for a specified user.
The return result is an instance of the L<apiData> class.

 Defined User Preference Attributes:
	user_name                : The users full name.
	user_first_name          : The users first name.
	user_last_name           : The users last name.
	user_address             : The address listed for the user.
	user_company             : The company the user works for.
	user_email               : The email address for the user.
	user_fax                 : The fax number for the user
	user_phone               : The telelphone number for the user.
	user_fontsize            : The fontsize the user has defined.
	user_read_security_value : The read security value for the user.

 Parameters:
	apiUser aUser     : The current api user's login data.
	scalar  userName  : The name of the user to get information on.
	scalar  prefName  : The name of the preference to retrieve.

 Returns: apiData
	the value of the user preference requested.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();
	
	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");


		my $tmp = $csapi->GetUserPreference($aUser, "u00001", "user_email");
	
		my $tmpstr = $tmp->getResponseData();
	};

	if ($@)
	{
		print $@;
	}

=cut


##############################################################################

=item B<GetValueListBox>

Get the contents of a ValueListbox.
The return result is an instance of the L<apiListObject> class.

 Parameters:
	apiUser aUser     : The current api user's login data.
	scalar  listObject: The ValueListbox to obtain.

 Returns: apiListObject
	the contents of the valuelistbox.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $list = $csapi->GetValueListBox($aUser, "date_keywords");

		for(my $i=0; $i < $list->getListboxSize(); $i++)
		{
			my $label = $list->getLabel($i);
			my $value = $list->getValue($i);

			print "GetValueListBox label $i: " . $label . "\n";
			print "GetValueListBox value $i: " . $value . "\n";		
		}
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<GetValueListBox>

Get the contents of a ValueListbox.
The return result is an instance of the L<apiListObject> class.

 Parameters:
	apiUser aUser     : The current api user's login data.
	scalar  listObject: The ValueListbox to obtain.
	scalar  configType: The config entry to search for the valueListbox in.  
	
	Valid Config Types: These are defined in the Globals class.
        $self->{ALL}       		// User, Shared and System. Returns the first one found.
        $self->{USER_PROFILE}	// A single users profile data.
        $self->{SHARED_PROFILE} // The shared profile data.
	    $self->{SYSTEM_CONFIG}  // The system config data.

 Returns: apiListObject
	the contents of the valuelistbox.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $globals = new ChangeSynergy::Globals();

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $list = $csapi->GetValueListBox($aUser, "user_defined_valuelistbox", $globals->{USER_PROFILE});

		for(my $i=0; $i < $list->getListboxSize(); $i++)
		{
			my $label = $list->getLabel($i);
			my $value = $list->getValue($i);

			print "GetValueListBox label $i: " . $label . "\n";
			print "GetValueListBox value $i: " . $value . "\n";		
		}
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<LoadConfigurationData>

Load configuration data on the SYNERGY/Change server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->LoadConfigurationData($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<LoadAllConfigurationFiles>

Loads all configuration data files on the SYNERGY/Change server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->LoadAllConfigurationFiles($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<LoadMergeConfigurationFiles>

Loads all configuration data files from the [CFG_MERGE][/CFG_MERGE] on the SYNERGY/Change server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->LoadMergeConfigurationFiles($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<LoadConfigurationFile>

Loads the specified configuration data file on the SYNERGY/Change server.
The pt.cfg, admin_framework.cfg, user_framework.cfg, and task_framework.cfg
configuration files are not allowed. The specified file must reside
in the "CS_HOME/cs_app/.../wsconfig" directory.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->LoadConfigurationFile($aUser, "my_config_file.cfg");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<LoadDatabaseListboxes>

All listboxes that get their values from a database will be reloaded.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->LoadDatabaseListboxes($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ReloadListboxes>

The pt_listbox.cfg file will be reloaded, and all listboxes
that get their values from a database will be reloaded.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ReloadListboxes($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ClearBusySessions>

Clears the busy session table.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ClearBusySessions($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ResetAdminTokens>

Logs-in the administrator user for all databases.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ResetAdminTokens($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ClearAllUserConfigurationData>

Unloads all user configuration data on the SYNERGY/Change server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ClearAllUserConfigurationData($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ClearTransitionUserList>

Clears the transition user list, a new copy will be created on the next request.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ClearTransitionUserList($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ResetConfigurationDataLoadTime>

Resets the loaded configuration data timestamp on the SYNERGY/Change server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ResetConfigurationDataLoadTime($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ResetLDAPPool>

Clears and reloads the LDAP session pool.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ResetLDAPPool($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ReloadStringTable>

Clears and reloads the external strings table.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ReloadStringTable($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ImportUsersFromAFile>

Import users into the Telelogic Directory Server from a file.  This
api does not allow the imported users to be assigned any roles; they
are merely imported from a file into the SDS with the specified values
or the defaults provided when calling this method. To assign roles,
use the web interface or add users using the AddUsers api.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser           : The current api user's login data.
	scalar  overwrite       : Should the import overwrite users currently on the 
	                          Telelogic Directory Server before.
  	scalar  importFile      : The path of a file to be used to import users.
	                          (ie., c:\\temp\\import_users.txt")
	scalar  importDelimiter : The delimiter used within the file to seperate the
	                          different import fields.
	scalar  importPassword  : The default password for all imported users if
	                          no password was supplied in the import file.
	scalar  importEmail     : The default e-mail address for all imported users
	                          if no e-mail address was supplied in the import file.
	scalar  importFirstname : The default first name for all imported users if no
	                          first name was supplied in the import file
	scalar  importLastname  : The default last name for all imported users if no
	                          last name was supplied in the import file
								 
 Returns: apiData
	the results of the import operation, "success" or an error message related to the
	problem.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");
		
		$importResults = $csapi->ImportUsersFromAFile($aUser, "false", "import_users.txt", ":", "password", "email", "firstname", "lastname");	

		print $importResults->getResponseData();

	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ImportUsersFromAllDatabases>

Import users into the Telelogic Directory Server from all databases to which
SYNERGY/Change is currently connected. The return result is an instance
of the L<apiData> class.

 Parameters:
	apiUser aUser           : The current api user's login data.
	scalar  overwrite       : Should the import overwrite users currently on the 
	                          Telelogic Directory Server before.
	scalar  importPassword  : The default password for all imported users.
	scalar  importEmail     : The default e-mail address for all imported users.
	scalar  importFirstname : The default first name for all imported users.
	scalar  importLastname  : The default last name for all imported users.
								 
 Returns: apiData
	the results of the import operation, "success" or an error message related to the
	problem.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");
		
		$importResults = $csapi->ImportUsersFromAllDatabases($aUser, "false", "password", "email", "firstname", "lastname");	

		print $importResults->getResponseData();
	
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ImportUsersFromCSLDAPServer>

Import users into the Telelogic Directory Server from a previsou Synergy Directory
Server (SDS). SDS was shipped with CS 4.3. When importing from SDS any user imported will
retain all of their user information, queries and reports. The return result is an instance
of the L<apiData> class.

 Parameters:
	apiUser aUser           : The current api user's login data.
	scalar  overwrite       : Should the import overwrite users currently on the 
	                          Telelogic Directory Server before.
	scalar  importURL       : The URL address of the SYNERGY/Change LDAP server to import users from.
	scalar  importEmail     : The default e-mail address for all imported users.
	scalar  importFirstname : The default first name for all imported users.
	scalar  importLastname  : The default last name for all imported users.
								 
 Returns: apiData
	the results of the import operation, "success" or an error message related to the
	problem.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");
		
		$importResults = $csapi->ImportUsersFromCSLDAPServer($aUser, "false", "ldap://maui:3892", "email", "firstname", "lastname");	

		print $importResults->getResponseData();
	
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ImmediateQueryHtml>

Run a SYNERGY/Change report, and wait for it to complete. This
api does not respond with a polling template. This api should
be used for running small reports. The return result is an 
instance of the L<apiData> class.

 Note: The return value is a complete HTML page. <HTML>...</HTML>
       The return value can be saved as a .html file, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser      : The current api user's login data.
	scalar  reportName : A SYNERGY/Change report name 
	                     (CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  queryString: A valid CMSynergy query string. 
	scalar  queryName  : A SYNERGY/Change query name 
	                     ([CCM_QUERY][NAME]query name[/NAME]...[/CCM_QUERY]).
	scalar  reportTitle: A title for this instance of the report.

 Returns: apiData
	the requested immediate query as an HTML page.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");
	
		my $tmpstr = $csapi->ImmediateQueryHtml($aUser, "Basic Summary", 
												"(submitter='cschuffe') and (cvtype='problem')",
												 undef, undef);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ImmediateReportHtml>

Run a SYNERGY/Change report, and wait for it to complete. This
api does not respond with a polling template. This api should
be used for running small reports. The return result is an 
instance of the L<apiData> class.

 Note: The return value is a complete HTML page. <HTML>...</HTML>
       The return value can be saved as a .html file, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser      : The current api user's login data.
	scalar  reportName : A SYNERGY/Change report name 
	                     ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  reportTitle: A title for this instance of the report.

 Returns: apiData
	the requested immediate query as an HTML page.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");
	
		my $tmpstr = $csapi->ImmediateReportHtml($aUser, "Basic Summary", "Basic Summary Report");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<InstallAPackage>

Install a SYNERGY/Change package. The return result is an 
instance of the L<apiData> class.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  packageName : The name of the package to install.

 Returns: apiData
	the results on if the package install was successful.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");
	
		my $results = $csapi->InstallAPackage($aUser, "dev_process");
		
		print $results->getResponseData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<LoadFormHtml>

Load any SYNERGY/Change template that does not require any other data
other than the template name and type. The return result is an instance 
of the L<apiData> class.

 Note: The return value is a complete HTML page. <HTML>...</HTML>
       The return value can be saved as a .html file, or loaded into 
	   a browser window/control.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  templateName: The name of the SYNERGY/Change template to load 
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).
	scalar  templateType: The type ([ONLOAD_ACTION]type[/ONLOAD_ACTION]) of the 
	                      SYNERGY/Change template to load.
 
 Returns: apiData
	the html template from the server.

 Example

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->LoadFormHtml($aUser, "SearchTipsWindow", "workspace_form");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<LoadFormUrl>

Load any SYNERGY/Change template that does not require any other data 
other than the template name and type. The return result is an instance of 
the L<apiData> class.

 Note: The return value is a complete URL address.
       The return value can be saved as a link, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  templateName: The name of the SYNERGY/Change template to load 
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).
	scalar  templateType: The type ([ONLOAD_ACTION]type[/ONLOAD_ACTION]) of the 
	                      SYNERGY/Change template to load.
 
 Returns: apiData
	the URL address for the desired template.

 Example

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->LoadFormUrl($aUser, "SearchTipsWindow", "workspace_form");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<LoadFrameSetHtml>

Load a SYNERGY/Change "frameset_form" template. The SYNERGY/Change server
parses the template name that was provided. The other function variables
are available to URLs contained in the frameset form definition.
The return result is an instance of the L<apiData> class.

 Note: The return value is a complete HTML page. <HTML>...</HTML>
       The return value can be saved as a .html file, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar templateName : The name of the SYNERGY/Change template to load
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).
	scalar taskNumber   : The Task ID to reference.
	scalar taskStatus   : The referenced Task's status value.
	scalar problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar problemStatus: The referenced CR's crstatus value.
	scalar cvid         : The CVID of a object to reference.
	scalar externalData : A string of XML data to pass to a submit request.

 Format of External Data XML:
 
 <EXTERNAL_CONTEXT_DATA>
 	<ATTRIBUTE NAME="attribute_name">your value</ATTRIBUTE>
 	<ATTRIBUTE NAME="attribute_name">your value</ATTRIBUTE>
 	<ATTRIBUTE NAME="attribute_name">your value</ATTRIBUTE>
 	.
 	.
 	.
 </EXTERNAL_CONTEXT_DATA>
 
 Returns: apiData
	the requested frameset as an HTML page.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->LoadFrameSetHtml($aUser, "ChangeSynergyShowDetails", undef, 
		                                      undef, "1347", undef, undef, undef);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<LoadFrameSetUrl>

Load a SYNERGY/Change "frameset_form" template. The SYNERGY/Change server
parses the template name that was provided. The other function variables
are available to URLs contained in the frameset form definition.
The return result is an instance of the L<apiData> class.

 Note: The return value is a complete URL address.
       The return value can be saved as a link, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar templateName : The name of the SYNERGY/Change template to load
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).
	scalar taskNumber   : The Task ID to reference.
	scalar taskStatus   : The referenced Task's status value.
	scalar problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar problemStatus: The referenced CR's crstatus value.
	scalar cvid         : The CVID of a object to reference.
	scalar externalData : A string of XML data to pass to a submit request.

 Format of External Data XML:
 
 <EXTERNAL_CONTEXT_DATA>
 	<ATTRIBUTE NAME="attribute_name">your value</ATTRIBUTE>
 	<ATTRIBUTE NAME="attribute_name">your value</ATTRIBUTE>
 	<ATTRIBUTE NAME="attribute_name">your value</ATTRIBUTE>
 	.
 	.
 	.
 </EXTERNAL_CONTEXT_DATA>
 
 Returns: apiData
	the requested frameset as URL.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->LoadFrameSetUrl($aUser, "ChangeSynergyShowDetails", undef, 
		                                      undef, "1347", undef, undef, undef);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<Login>

Login to a SYNERGY/Change server as a specific user and connect to a 
specific CMSynergy database. The return result is an instance of the L<apiUser> class.

 Parameters:
	scalar user    : The name of the user.
	scalar password: The password for the user.
	scalar role    : The role for the user.
	scalar database: The CMSynergy database path for the user.

 Returns: apiUser
	a new instance of a apiUser class with the specified information.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ModifyCR>

Apply the modified Change Request data. Only data objects that have been
flagged as modified are submitted to the SYNERGY/Change server.
The attributes problem_number, modify_time, and cvid, should not be
altered. The api classes will automatically process these attributes when needed.
The return result is an instance of the L<apiData> class.

Note: The apiObjectData's member method setValue("") will automatically set
the modified flag when invoked.

 Parameters:
	apiUser         aUser: The current api user's login data.
	apiObjectVector data : The data to be processed by the api function.

 Returns: apiData
	results on if the modify was successful
 
 Example:
 
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->AttributeModifyCRData($aUser, "100", "crstatus");
		or
		my $tmp = $csapi->AttributeModifyCRData($aUser, "100");
		or
		my $tmp = $csapi->ModifyCRData($aUser, "100", "CRDetail");
		or
		my $tmp = $csapi->GetCRData($aUser, "100", "problem_synopsis|problem_description|keyword");
		
		$tmp->getDataObjectByName("problem_synopsis")->setValue("I modified the synopsis through the csapi...");
		$tmp->getDataObjectByName("problem_description")->setValue("I modified the description through the csapi...");
		$tmp->getDataObjectByName("keyword")->setValue("csapi");

		my $tmpstr = $csapi->ModifyCR($aUser, $tmp);

	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ModifyCRData>

Load the details of a Change Request into data classes in which the 
details of the Change Request can be modified. The modified data classes
can then be submitted using one of the modification api functions 
to change a Change Request. The return result is an instance of
the L<apiObjectVector> class.


Note: Current transition choices are provided with this api function call.
See L<apiTransitions> class description.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar  templateName : The name of the SYNERGY/Change template to load 
	                       ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).

 Returns: apiObjectVector
	the details of a change request in data format.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->ModifyCRData($aUser, "100", "CRDetail");

		my $tmpstr = tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ModifyObjectAttributes>

Modifies existing attribute(s) of compver with name "your name value." The value(s) given
to the attribute must be provided. This operation also updates the compver's modify_time 
attribute. The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser         aUser       : The current api user's login data.
	scalar          cvidList    : A "|" pipe delimited list of cvids to be affected, or a single cvid.
	apiObjectVector attrData    : The data to be processed by the api function.
 
 Returns: apiData
	The return message from the server.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $attrData = new ChangeSynergy::apiObjectVector();

		my $objData = new ChangeSynergy::apiObjectData();
		$objData->setName("attribute_a");
		$objData->setValue("Linux");
		$attrData->addDataObject($objData);

		my $objData = new ChangeSynergy::apiObjectData();
		$objData->setName("attribute_b");
		$objData->setValue("true");
		$attrData->addDataObject($objData);

		my $objData = new ChangeSynergy::apiObjectData();
		$objData->setName("attribute_c");
		$objData->setValue("777");
		$attrData->addDataObject($objData);

		my $tmp = $csapi->ModifyObjectAttributes($aUser, "10156|10157|10158|10159|10160", $attrData)

		print $tmp->getResponseData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ModifyTask>

Apply the modified Task data. Only data objects that have been flagged
as modified are submitted to the SYNERGY/Change server. The attributes
task_number, modify_time, and cvid, should not be altered. The api
classes will automatically process these attributes when needed.
The return result is an instance of the L<apiData> class.

Note: The L<apiObjectData>'s member method setValue("") will automatically set
the modified flag when invoked.

 Parameters:
	apiUser         aUser: The current api user's login data.
	apiObjectVector data : The data to be processed by the api function.

 Returns: apiData
	results on if the modify was successful

 Example:
 
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->AttributeModifyTaskData($aUser, "10", "status");
		or
		my $tmp = $csapi->AttributeModifyTaskData($aUser, "10");
		or
		my $tmp = $csapi->ModifyTaskData($aUser, "10", "TaskDetails");
		or
		my $tmp = $csapi->GetTaskData($aUser, "10", "task_synopsis|task_description|priority");
		
		tmp->getDataObjectByName("task_synopsis")->setValue("I modified the synopsis through the csapi...");
		tmp->getDataObjectByName("task_description")->setValue("I modified the description through the csapi...");
		tmp->getDataObjectByName("priority")->setValue("high");

		my $tmpstr = $csapi->ModifyTask($aUser, $tmp);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ModifyTaskData>

Load the details of a Task into data classes in which the details of
the Task can be modified. The modified data classes can then be 
submitted using one of the modification api functions to change a Task.
The return result is an instance of the L<apiObjectVector> class.


 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  taskNumber  : The Task ID to reference.
	scalar  templateName: The name of the SYNERGY/Change template to load
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).
 
 Returns: apiObjectVector
	the details of a task in data format

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->ModifyTaskData($aUser, "10", "TaskDetails");

		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

#############################################################################

=item B<PreferenceNameSubstitutionForAllUsers>

Make a preference name substitution for all users with in a preference name.
One of the most useful uses of this function is when a databases path
changes, the database path in the user's config can be updated. It finds
and replaces all occurrences of one string for another string. The return 
result is an instance of the L<apiData> class.

Note: It is not possible to change or add user profile values.  These values
are the users first names, last names, email addresses, fax numbers, telephone
numbers and addresses.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  keyValue: The value to search for when doing a replacement.
	scalar  subValue: The replacement value, the value to be added.

 Returns: apiData
	the return message from the server.
 
 Example:
	
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		$tmpData = $csapi->PreferenceNameSubstitutionForAllUsers($aUser, "\\\\angler\\ccmdb\\cm_database", "\\\\angler\\cm_database");
	
		print $tmpData->getResponseData();

	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<PreferenceNameSubstitutionForAUser>

Make a preference name substitution for a user with in a preference name.
One of the most useful uses of this function is when a databases path
changes, the database path in the user's config can be updated.  It finds and
replaces all occurrences of one string for another string. The return result
is an instance of the L<apiData> class.

Note: It is not possible to change or add user profile values.  These values
are the users first names, last names, email addresses, fax numbers, telephone
numbers and addresses.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  username: The name of the user's preferences to edit.
	scalar  keyValue: The value to search for when doing a replacement.
	scalar  subValue: The replacement value, the value to be added.

 Returns: apiData
	the return message from the server.
 
 Example:
	
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		$tmpData = $csapi->PreferenceNameSubstitutionForAUser($aUser, "u00001", "\\\\angler\\ccmdb\\cm_database", "\\\\angler\\cm_database");
	
		print $tmpData->getResponseData();

	};

	if ($@)
	{
		print $@;
	}

=cut

#############################################################################

=item B<PreferenceSubstitutionForAUser>

Given a user preference, find and replace all occurrences of one string
for another string. This is helpful when you need to change a user's config
entry to replace one report name for another report name throughout their
_USER_CFG entry. The return result is an instance of the L<apiData> class.

Note: It is not possible to change or add user profile values.  These values
are the users first names, last names, email addresses, fax numbers, telephone
numbers and addresses.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  username: The name of the user's preferences to edit.
	scalar  keyName : The name of the preference to edit.
	scalar  keyValue: The value to search for when doing a replacement.
	scalar  subValue: The replacement value, the value to be added.
	scalar  allDBs  : true or false, should the add take place for all databases
						or just the one that the current api user is logged into.

 Returns: apiData
	the return message from the server.
 
 Example:
	
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");
		
		$tmpData = $csapi->PreferenceSubstitutionForAUser($aUser, "u00001", "_USER_CFG_", "problem_review", "problems_review", "true");
	
		print $tmpData->getResponseData();

	};

	if ($@)
	{
		print $@;
	}

=cut

#############################################################################

=item B<PreferenceSubstitutionForAllUsers>

Given a user preference, find and replace all occurrences of one string
for another string. This is helpful when you need to change all users' config
entries to replace one report name for another report name throughout their
_USER_CFG entries. The return result is an instance of the L<apiData> class.

Note: It is not possible to change or add user profile values.  These values
are the users first names, last names, email addresses, fax numbers, telephone
numbers and addresses.

 Parameters:
	apiUser aUser   : The current api user's login data.
	scalar  keyName : The name of the preference to edit.
	scalar  keyValue: The value to search for when doing a replacement.
	scalar  subValue: The replacement value, the value to be added.
	scalar  allDBs  : true or false, should the add take place for all databases
						or just the one that the current api user is logged into.

 Returns: apiData
	the return message from the server.
 
 Example:
	
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");
		
		$tmpData = $csapi->PreferenceSubstitutionForAllUsers($aUser, "_USER_CFG_", "problem_review", "problems_review", "true");
	
		print $tmpData->getResponseData();

	};

	if ($@)
	{
		print $@;
	}

=cut

#############################################################################


=item B<ProcessEmailSubmitForms>

Process email submit forms on the SYNERGY/Change server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ProcessEmailSubmitForms($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<QueryData>

Run a SYNERGY/Change report, and respond with XML data only.
The return result is an instance of the L<apiQueryData> class.

Note: The return value is the complete contents of the report represented as data only.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  reportName  : A ChangeSynergy report name 
	                      ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  queryString : A valid CMSynergy query string. 
	scalar  queryName   : A ChangeSynergy query name 
	                      ([CCM_QUERY][NAME]query name[/NAME]...[/CCM_QUERY]).
	scalar  reportTitle : A title for this instance of the report.
	scalar  templateName: The name of the ChangeSynergy template to load
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).
	

 Returns: apiQueryData
	the XML data that represents the report data.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->QueryData($aUser, "Basic Summary", "(submitter='cschuffe') and (cvtype='problem')", 
                                    undef, undef, undef);
	};

	if ($@)
	{
		print $@;
	}

=cut

#############################################################################

=item B<QueryData>

Run a ChangeSynergy report, and respond with XML data only.
The return result is an instance of the L<apiQueryData> class.

Note: The return value is the complete contents of the report represented as data only.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  reportName   : A ChangeSynergy report name 
	                       ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  queryString  : A valid CMSynergy query string. 
	scalar  queryName    : A ChangeSynergy query name 
	                       ([CCM_QUERY][NAME]query name[/NAME]...[/CCM_QUERY]).
	scalar  reportTitle  : A title for this instance of the report.
	scalar  templateName : The name of the ChangeSynergy template to load
	                       ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).
	scalar  attributeList: A piped list of attributes "problem_number|crstatus|assigner...".
	

 Returns: apiQueryData
	the XML data that represents the report data.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->QueryData($aUser, "Basic Summary", "(submitter='cschuffe') and (cvtype='problem')", 
                                    undef, undef, undef, "problem_number|crstatus");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<QueryHtml>

Run a ChangeSynergy report, and respond with a polling template.
This api should be used for running large reports. The return result 
is an instance of the L<apiData> class.

 Note: The return value is a complete HTML page. <HTML>...</HTML>
       The return value can be saved as an .html file, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  reportName  : A ChangeSynergy report name 
	                      ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  queryString : A valid CMSynergy query string. 
	scalar  queryName   : A ChangeSynergy query name 
	                      ([CCM_QUERY][NAME]query name[/NAME]...[/CCM_QUERY]).
	scalar  reportTitle : A title for this instance of the report.
	scalar  templateName: The name of the ChangeSynergy template to load 
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).

 Returns: apiData
	the polling template for the query which was run.  This is an HTML page.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->QueryHtml($aUser, "Basic Summary", 
                                       "(submitter='cschuffe') and (cvtype='problem')",
                                       undef, "Basic Summary Report");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<QueryNameData>

Run a ChangeSynergy report, and respond with XML data only.
The return result is an instance of the L<apiQueryData> class.

Note: The return value is the complete contents of the report represented as data only.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  reportName   : A ChangeSynergy report name 
	                       ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  queryName    : A ChangeSynergy query name 
	                       ([CCM_QUERY][NAME]query name[/NAME]...[/CCM_QUERY]).
	scalar  attributeList: A piped list of attributes "problem_number|crstatus|assigner...".
	

 Returns: apiQueryData
	the XML data that represents the report data.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->QueryNameData($aUser, "Basic Summary", "All CRs", "problem_number|crstatus");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<QueryStringData>

Run a ChangeSynergy report, and respond with XML data only.
The return result is an instance of the L<apiQueryData> class.

Note: The return value is the complete contents of the report represented as data only.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  reportName   : A ChangeSynergy report name 
	                       ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  queryString  : A valid CMSynergy query string. 
	scalar  attributeList: A piped list of attributes "problem_number|crstatus|assigner...".
	

 Returns: apiQueryData
	the XML data that represents the report data.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->QueryStringData($aUser, "Basic Summary", "(submitter='cschuffe') and (cvtype='problem')", 
                                    "problem_number|crstatus");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<RefreshUsers>

Causes all backend sessions to refresh their security settings and
reload all user information. This is needed if new users are added to
SYNERGY/CM outside of SYNERGY/Change. Normally, these changes will only be
seen when new sessions are started; existing sessions will continue to use
the stale data. This function forces all sessions to refresh
themselves and immediately see such changes.

Requires the user login with the Admin role.

This call is not needed when users are added via the SYNERGY/Change
web interface or with a CSAPI function like AddUser.

SYNERGY/Change will not recognize users without an entry in its LDAP server.
Simply adding users to SYNERGY/CM and calling this function will not
allow those users to log on to SYNERGY/Change. This function is only useful
during advanced user customization.

 Parameters:
	apiUser aUser        : The current API user's login data.

 Returns: scalar
	a return message from the server.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		$csapi->RefreshUsers($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ReportData>

Run a ChangeSynergy report, and respond with XML data only.
The return result is an instance of the L<apiQueryData> class.

Note: The return value is the complete contents of the report represented as data only.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  reportName   : A ChangeSynergy report name 
	                       ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  attributeList: A piped list of attributes "problem_number|crstatus|assigner...".

 Returns: apiQueryData
	the XML data that represents the report data.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->ReportData($aUser, "DRP - Summary of CRs Submitted by Me", "problem_number");
		
		$tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ReportData>

Run a ChangeSynergy report, and respond with XML data only.
The return result is an instance of the L<apiQueryData> class.

Note: The return value is the complete contents of the report represented as data only.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  reportName  : A ChangeSynergy report name 
	                      ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  reportTitle : A title for this instance of the report.
	scalar  templateName: The name of the ChangeSynergy template to load 
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).

 Returns: apiQueryData
	the XML data that represents the report data.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->ReportData($aUser, "DRP - Summary of CRs Submitted by Me", undef, undef);
		
		$tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ReportData>

Run a ChangeSynergy report, and respond with XML data only.
The return result is an instance of the L<apiQueryData> class.

Note: The return value is the complete contents of the report represented as data only.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  reportName   : A ChangeSynergy report name 
	                       ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  reportTitle  : A title for this instance of the report.
	scalar  templateName : The name of the ChangeSynergy template to load 
	                       ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).
	scalar  attributeList: A piped list of attributes "problem_number|crstatus|assigner...".

 Returns: apiQueryData
	the XML data that represents the report data.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->ReportData($aUser, "DRP - Summary of CRs Submitted by Me", undef, undef, undef);
		
		$tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ReportHtml>

Run a ChangeSynergy report, and respond with a polling template.
This api should be used for running large reports. The return result
is an instance of the L<apiData> class.

 Note: The return value is a complete HTML page. <HTML>...</HTML>
       The return value can be saved as an .html file, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  reportName  : A ChangeSynergy report name 
	                      ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  reportTitle : A title for this instance of the report.
	scalar  templateName: The name of the ChangeSynergy template to load
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).

 
 Returns: apiData
	the polling template for the report which was run.  This is an HTML page.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ReportHtml($aUser, "Basic Summary", "Basic Summary Report", undef);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ReportOnCRData>

Run a ChangeSynergy report that reports on a single Change Request.
The return result is an instance of the L<apiQueryData> class.

Note: The return value is the complete contents of the report represented as data only.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar  ReportName   : A ChangeSynergy report name
	                       ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  reportTitle  : A title for this instance of the report.

 Returns: apiQueryData
	the xml data that represents the contents of the report.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->ReportOnCRData($aUser, "132", "DRP - Summary with Tasks and Objects", undef);
		
		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ReportOnCRData>

Run a ChangeSynergy report that reports on a single Change Request.
The return result is an instance of the L<apiQueryData> class.

Note: The return value is the complete contents of the report represented as data only.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar  ReportName   : A ChangeSynergy report name
	                       ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  reportTitle  : A title for this instance of the report.
	scalar  attributeList: A piped list of attributes "problem_number|crstatus|assigner...".

 Returns: apiQueryData
	the xml data that represents the contents of the report.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->ReportOnCRData($aUser, "132", "DRP - Summary with Tasks and Objects",
                                         undef, "problem_number|crstatus");
		
		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ReportOnCRHtml>

Run a ChangeSynergy report that reports on a single Change Request.
The return result is an instance of the L<apiData> class.

 Note: The return value is a complete HTML page. <HTML>...</HTML>
       The return value can be saved as a .html file, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar  reportName   : A ChangeSynergy report name 
	                       ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  reportTitle  : A title for this instance of the report.
 
 Returns: apiData
	the report as an HTML page.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ReportOnCRHtml($aUser, "1347", "problemdetail", undef);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ReportOnObjectData>

Run a ChangeSynergy report that reports on a single Object.
The return result is an instance of the L<apiQueryData> class.

Note: The return value is the complete contents of the report represented as data only.

 Parameters:
	apiUser aUser      : The current api user's login data.
	scalar  objectId   : The CVID of the referenced object.
	scalar  reportName : A ChangeSynergy report name 
	                     ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  reportTitle: A title for this instance of the report.

 Returns: apiQueryData
	the report in xml data format.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->ReportOnObjectData($aUser, "11753", "objectdetail", undef);
		
		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ReportOnObjectData>

Run a ChangeSynergy report that reports on a single Object.
The return result is an instance of the L<apiQueryData> class.

Note: The return value is the complete contents of the report represented as data only.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  objectId     : The CVID of the referenced object.
	scalar  reportName   : A ChangeSynergy report name
	                       ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  reportTitle  : A title for this instance of the report.
	scalar  attributeList: A piped list of attributes "problem_number|crstatus|assigner...".

 Returns: apiQueryData
	the report in xml data format.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->ReportOnObjectData($aUser, "11753", "objectdetail", undef, "problem_number");
		
		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ReportOnObjectHtml>

Run a ChangeSynergy report that reports on a single Object.
The return result is an instance of the L<apiData> class.

 Note: The return value is a complete HTML page. <HTML>...</HTML>
       The return value can be saved as a .html file, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser      : The current api user's login data.
	scalar  objectId   : The CVID of the referenced object.
	scalar  reportName : A ChangeSynergy report name
	                     ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  reportTitle: A title for this instance of the report.

 Returns: apiData
	the report as an HTML page.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ReportOnObjectHtml($aUser, "13", "objectdetail", undef);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ReportOnTaskData>

Run a ChangeSynergy report that reports on a single Task.
The return result is an instance of the L<apiQueryData> class.

 Parameters:
	apiUser aUser      : The current api user's login data.
	scalar  taskNumber : The Task ID to reference.
	scalar  reportName : A ChangeSynergy report name
	                     ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  reportTitle: A title for this instance of the report.

 Returns: apiQueryData
	the report in xml data format.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->ReportOnTaskData($aUser, "1", "taskdetail", undef);
		
		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ReportOnTaskData>

Run a ChangeSynergy report that reports on a single Task.
The return result is an instance of the L<apiQueryData> class.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  taskNumber   : The Task ID to reference.
	scalar  reportName   : A ChangeSynergy report name
	                       ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  reportTitle  : A title for this instance of the report.
	scalar  attributeList: A piped list of attributes "problem_number|crstatus|assigner...".

 Returns: apiQueryData
	the report in xml data format.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->ReportOnTaskData($aUser, "1", "taskdetail", undef, "task_number");
		
		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ReportOnTaskHtml>

Run a ChangeSynergy report that reports on a single Task.
The return result is an instance of the L<apiData> class.

 Note: The return value is a complete HTML page. <HTML>...</HTML>
       The return value can be saved as a .html file, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser      : The current api user's login data.
	scalar  taskNumber : The Task ID to reference.
	scalar  reportName : A ChangeSynergy report name
	                     ([CCM_REPORT][NAME]report name[/NAME]...[/CCM_REPORT]).
	scalar  reportTitle: A title for this instance of the report.

 Returns: apiData
	the results of the report as an HTML page.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ReportOnTaskHtml($aUser, "13", "taskdetail", undef);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ServerAPIVersion>

Get the API version number of the server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	The version number string.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr1 = $csapi->ServerAPIVersion($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ServerGetFile>

Get a file object from the ChangeSynergy server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.
	scalar  file : The file name of the object to retrieve.

 Returns: apiData
	the byte data returned by the server.
	
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser      = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");
		my $file       = "serverFile.txt";
		my $filehandle = $csapi->ServerGetFile($aUser, $file);

		open(OUTPUTFILE, ">serverFile.txt");

		print OUTPUTFILE $filehandle->getResponseByteData();

		close OUTPUTFILE;
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ServerSendFile>

Copy a file object to the ChangeSynergy server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser : The current api user's login data.
	scalar  buffer: The BYTE data to send to the server.
	scalar  size  : The size of the BYTE data.

 Returns: apiData
	the return message from the server.
	
 Example:

	my $csapi  = new ChangeSynergy::csapi();
	my $buffer = "";
	my $buf    = "";
	my $size   = "";

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser      = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		open(INPUTFILE, "filename.txt") or die "Could not open up the file";

		while($buf = readline *INPUTFILE)
		{
			$buffer .= $buf;
		}

		close(INPUTFILE);
		
		$size = -s "filename.txt";

		my $filehandle = $csapi->ServerSendFile($aUser, $buffer, $size);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<SetAttributes>

Sets/creates ChangeSynergy attributes on the server. 

This operation is not needed if all attributes referenced by your custom application are
defined in a installed CRProcess. The GetAttributes() api method can be used to confirm this.

The unique list of attributes provided will be stored in a ChangeSynergy configuration file with
the name provided. The "lpszCfgName" should not include a ".ext" dot extension, it should be just
a file name prefix, ex: "my_app_attrs". A ".cfg" will be added to the name by the SYNERGY/Change server.
Care should be given to naming the file. The names: 'pt', 'task_framework', 'admin_framework',
'user_framework', 'users', and 'template', are reserved system configuration file names, and are not
allowed. The operation will DELETE a file of name lpszCfgName.cfg if it exists. This is so you can
overwrite your own custom attribute list. The operation will fail if the file cannot be created or deleted.

The operation will fail if any of the listed attributes exist on the server outside of any defined
in a existing lpszCfgName.cfg file name. The list of offending attributes will be returned if the
operation fails for this reason. It is recommended that the GetAttributes() api method be used to confirm
that all custom application attributes are in fact not known to the SYNERGY/Change server.

Known predefined ChangeSynergy attributes (reserved, and cannot be defined):

	***************** Global CR attributes *****************
	
	[CCM_ATTRIBUTE][NAME]crstatus[/NAME][ALIAS]Status[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]problem_synopsis[/NAME][ALIAS]Synopsis[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]problem_description[/NAME][ALIAS]Problem Description[/ALIAS][TYPE]CCM_TEXT[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]problem_number[/NAME][ALIAS]CR ID[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]transition_log[/NAME][ALIAS]Log[/ALIAS][TYPE]CCM_TEXT[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]submitter[/NAME][ALIAS]Submitter[/ALIAS][TYPE]CCM_USER[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]submitter_name[/NAME][ALIAS]Name[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]submitter_phone[/NAME][ALIAS]Phone Number[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]submitter_fax[/NAME][ALIAS]Fax Number[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]submitter_address[/NAME][ALIAS]Address[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]submitter_email[/NAME][ALIAS]Email Address[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]submitter_company[/NAME][ALIAS]Employer[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	
	 ***************** Global Task attributes *****************

	[CCM_ATTRIBUTE][NAME]task_number[/NAME][ALIAS]Task Number[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]task_synopsis[/NAME][ALIAS]Synopsis[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	
	***************** Global Object attributes *****************
	
	[CCM_ATTRIBUTE][NAME]cvid[/NAME][ALIAS]CM Synergy ID[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]comment[/NAME][ALIAS]Object Comment[/ALIAS][TYPE]CCM_TEXT[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]description[/NAME][ALIAS]Object Description[/ALIAS][TYPE]CCM_TEXT[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]displayname[/NAME][ALIAS]Display Name[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]source[/NAME][ALIAS]Source[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]attachment_name[/NAME][ALIAS]Attachment Name[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]attachment_size[/NAME][ALIAS]Attachment Length[/ALIAS][TYPE]CCM_NUMBER[/TYPE][/CCM_ATTRIBUTE]
	
	***************** Shared Ccm/PT/System attributes *****************
	
	[CCM_ATTRIBUTE][NAME]status[/NAME][ALIAS]Status[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]database[/NAME][ALIAS]Database[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]modifiable_in[/NAME][ALIAS]Work in DB[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]created_in[/NAME][ALIAS]Created in DB[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]cvtype[/NAME][ALIAS]Object Type[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]name[/NAME][ALIAS]Object Name[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]modify_time[/NAME][ALIAS]Last Modified Time[/ALIAS][TYPE]CCM_DATE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]status_log[/NAME][ALIAS]Transition Log[/ALIAS][TYPE]CCM_TEXT[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]platform[/NAME][ALIAS]Platform[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]creator[/NAME][ALIAS]Creator[/ALIAS][TYPE]CCM_USER[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]create_time[/NAME][ALIAS]Created Date[/ALIAS][TYPE]CCM_DATE[/TYPE][/CCM_ATTRIBUTE]
	
	***************** Special PTCLI/System Attributes *****************
	
	[CCM_ATTRIBUTE][NAME]users_roles[/NAME][ALIAS]User Roles[/ALIAS][TYPE]CCM_TEXT[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]users[/NAME][ALIAS]Users[/ALIAS][TYPE]CCM_TEXT[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]user[/NAME][ALIAS]User[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]generic_cs_attribute[/NAME][ALIAS]Do Not Use/Remove[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]dcm_dbid[/NAME][ALIAS]DCM Database ID[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]dcm_delimiter[/NAME][ALIAS]DCM Delimiter[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]pt_app[/NAME][ALIAS]DevClient Application Data[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]pt_app_role[/NAME][ALIAS]DevClient Application Role[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]all_databases[/NAME][ALIAS]All Databases[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]all_groups[/NAME][ALIAS]All Groups[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]LIFECYCLES[/NAME][ALIAS]All Lifecycles[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]LIFECYCLE_STATES[/NAME][ALIAS]All States in a Lifecycle[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]LIFECYCLE_TRANSITIONS[/NAME][ALIAS]All Transitions in a Lifecycle[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]VALID_TRANSITIONS[/NAME][ALIAS]Allowable Transitions[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]VALID_CREATES[/NAME][ALIAS]Allowable Submissions[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]VALID_CREATES_USER[/NAME][ALIAS]Allowable Submissions for User[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]CURRENT_LIFECYCLE[/NAME][ALIAS]Current Lifecycle[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]IS_ADMIN[/NAME][ALIAS]Is a Admin[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]licensed_dcmpt[/NAME][ALIAS]License Info[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]licensed_xpt[/NAME][ALIAS]License Info[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]licensed_grpsec[/NAME][ALIAS]License Info[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	
	***************** Special ACcent Attributes *****************
	
	[CCM_ATTRIBUTE][NAME]_COMMENTS[/NAME][ALIAS]Comments[/ALIAS][TYPE]CCM_TEXT[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]_DUPLICATE[/NAME][ALIAS]Duplicate[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]_CREATE_TASK[/NAME][ALIAS]Create Task[/ALIAS][TYPE]CCM_TOGGLE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]_IS_MODIFIABLE[/NAME][ALIAS]Object can be Modified[/ALIAS][TYPE]CCM_TOGGLE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]IS_MODIFIABLE[/NAME][ALIAS]Object can be Modified[/ALIAS][TYPE]CCM_TOGGLE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]has_duplicate[/NAME][ALIAS]Duplicate of[/ALIAS][TYPE]CCM_RELATION[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]attachment[/NAME][ALIAS]Attachment(s)[/ALIAS][TYPE]CCM_RELATION[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]associated_task[/NAME][ALIAS]Associated Task(s)[/ALIAS][TYPE]CCM_RELATION[/TYPE][/CCM_ATTRIBUTE]
	
	***************** Special ChangeSynergy Identifiers *****************
	
	[CCM_ATTRIBUTE][NAME]_ATTACHMENT_NAME[/NAME][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]_ATTACHMENT_COMMENT[/NAME][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]_ATTACHMENT_IS_BINARY[/NAME][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]_ATTACHMENT_IS_ASCII[/NAME][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]_ATTACHMENT_TYPE[/NAME][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]START_HERE[/NAME][ALIAS]Submit Forms[/ALIAS][TYPE]CCM_VALUELISTBOX[/TYPE][/CCM_ATTRIBUTE]
	
	***************** Textual Replacement Variables *****************
	
	[CCM_ATTRIBUTE][NAME]ChangeRequestProcessImage[/NAME][ALIAS]no_cr_process.gif[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	
	***************** Textual Replacement Variables *****************
	
	[CCM_ATTRIBUTE][NAME]Problem_Identifier[/NAME][ALIAS]Change Request[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]Problem_Identifier_Plural[/NAME][ALIAS]Change Requests[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]Problem_Identifier_Abbr[/NAME][ALIAS]CR[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	
	***************** Textual Replacement Variables *****************
	
	[CCM_ATTRIBUTE][NAME]DUPLICATE[/NAME][ALIAS]Duplicate Of[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]QUERY_STRING[/NAME][ALIAS]Query String[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]cr_modifications[/NAME][ALIAS]Show Modify Events[/ALIAS][TYPE]CCM_TOGGLE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]cr_transitions[/NAME][ALIAS]Show Transition Comments[/ALIAS][TYPE]CCM_TOGGLE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]cr_notes[/NAME][ALIAS]Show Notes[/ALIAS][TYPE]CCM_TOGGLE[/TYPE][/CCM_ATTRIBUTE]
	
	***************** Utility *****************
	
	[CCM_ATTRIBUTE][NAME]TRANSITION_USER[/NAME][ALIAS]Transition User[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	
	***************** Profile Attributes *****************
	
	[CCM_ATTRIBUTE][NAME]report_window_target[/NAME][ALIAS]Report Window Target[/ALIAS][TYPE]CCM_VALUELISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]report_link_target[/NAME][ALIAS]Report Link Target[/ALIAS][TYPE]CCM_VALUELISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]fontsize[/NAME][ALIAS]Font Size[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]user_default_home_page[/NAME][ALIAS]Report Link Target[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]defaultReport[/NAME][ALIAS]Default Report[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]reportIncremental[/NAME][ALIAS]Incremental Report[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]reportIncrementalSize[/NAME][ALIAS]Incremental Report Size[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]object_scope[/NAME][ALIAS]Object Scope[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]object_scope_lifecycle[/NAME][ALIAS]Object Scope Lifecycle[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]cr_notes[/NAME][ALIAS]CR Notes[/ALIAS][TYPE]CCM_TOGGLE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]cr_transitions[/NAME][ALIAS]CR Transition[/ALIAS][TYPE]CCM_TOGGLE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]cr_modifications[/NAME][ALIAS]CR Modifications[/ALIAS][TYPE]CCM_TOGGLE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]firstname[/NAME][ALIAS]User's first name[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]lastname[/NAME][ALIAS]User's last name[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	
	***************** Task attributes *****************
	
	[CCM_ATTRIBUTE][NAME]task_subsys[/NAME][ALIAS]Task Sub-System[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]task_description[/NAME][ALIAS]Description[/ALIAS][TYPE]CCM_TEXT[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]priority[/NAME][ALIAS]Priority[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]est_completion_date[/NAME][ALIAS]Estimated Completion Date[/ALIAS][TYPE]CCM_DATE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]est_duration[/NAME][ALIAS]Estimated Duration[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]actual_duration[/NAME][ALIAS]Actual Duration[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]registration_date[/NAME][ALIAS]Registration Date[/ALIAS][TYPE]CCM_DATE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]completion_date[/NAME][ALIAS]Completion Date[/ALIAS][TYPE]CCM_DATE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]asgndate_begin[/NAME][ALIAS]Assigned After[/ALIAS][TYPE]CCM_DATE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]asgndate_end[/NAME][ALIAS]Assigned Before[/ALIAS][TYPE]CCM_DATE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]compdate_begin[/NAME][ALIAS]Completed After[/ALIAS][TYPE]CCM_DATE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]compdate_end[/NAME][ALIAS]Completed Before[/ALIAS][TYPE]CCM_DATE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]completed_id[/NAME][ALIAS]Completed Identification[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]completed_in[/NAME][ALIAS]Completed In[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]assigner[/NAME][ALIAS]Assigner[/ALIAS][TYPE]CCM_USER[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]resolver[/NAME][ALIAS]Resolver[/ALIAS][TYPE]CCM_USER[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]assignment_date[/NAME][ALIAS]Assignment Date[/ALIAS][TYPE]CCM_DATE[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]release[/NAME][ALIAS]Release[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]keyword[/NAME][ALIAS]Keyword[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	
	***************** Object attributes *****************
	
	[CCM_ATTRIBUTE][NAME]owner[/NAME][ALIAS]Owner of Object[/ALIAS][TYPE]CCM_USER[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]subsystem[/NAME][ALIAS]Sub-System[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]version[/NAME][ALIAS]Object Version[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]type[/NAME][ALIAS]Object Type[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]description[/NAME][ALIAS]Folder Description[/ALIAS][TYPE]CCM_TEXT[/TYPE][/CCM_ATTRIBUTE]
	
	***************** Textual Replacement Variables *****************
	
	[CCM_ATTRIBUTE][NAME]ASSOCIATED_TASK[/NAME][ALIAS]Associated Task[/ALIAS][TYPE]CCM_STRING[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]associated_cv[/NAME][ALIAS]Associated Object(s)[/ALIAS][TYPE]CCM_RELATION[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]has_associated_task[/NAME][ALIAS]Associated CR(s)[/ALIAS][TYPE]CCM_RELATION[/TYPE][/CCM_ATTRIBUTE]
	
	***************** Utility *****************
	
	[CCM_ATTRIBUTE][NAME]TASKSTATES[/NAME][ALIAS]Task States[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]TASK_DATABASE[/NAME][ALIAS]Task Database[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]all_releases[/NAME][ALIAS]All Releases[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]inactive_releases[/NAME][ALIAS]Inactive Releases[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]
	[CCM_ATTRIBUTE][NAME]active_releases[/NAME][ALIAS]Active Releases[/ALIAS][TYPE]CCM_LISTBOX[/TYPE][/CCM_ATTRIBUTE]

A ChangeSynergy attribute is:

	[CCM_ATTRIBUTE]
		[NAME]
			The ChangeSynergy Attribute name.
		[/NAME]
		[TYPE]
			The Web visualization data type, 
			available types are: CCM_STRING, CCM_TEXT, CCM_LISTBOX,
			and CCM_VALUELISTBOX.
		[/TYPE]
		[ROLE NAME]
			Optional role based aliases.
			There can be as many role options as there are defined web roles.
			Where "ROLE NAME" and "/ROLE NAME" are the literal role name.
		[/ROLE NAME]...
		[ALIAS]
			The default alias value for the attribute. This value is returned
			if role options are not used or if the users role is not specified.

			The [ALIAS] tag set defines the default, if no [ALIAS] tag exists
			the [NAME] is returned.
		[/ALIAS]
	[/CCM_ATTRIBUTE]

The [NAME] is identified through the getName() method.
The [TYPE] is identified through the getType() method.
The [ALIAS] is identified through the getLabel() method.
The [ROLE NAME] option is not available through the api.

The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser         aUser   : The current api user's login data.
	apiObjectVector attrData: The data to be processed by the api function.
 
 Returns: apiData
	The return message from the server.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $attrData = new ChangeSynergy::apiObjectVector();

		my $objData = new ChangeSynergy::apiObjectData();
		$objData->setName("cost");
		$objData->setType("CCM_STRING");
		$objData->setLabel("Cost");
		$attrData->addDataObject($objData);

		my $objData = new ChangeSynergy::apiObjectData();
		$objData->setName("customer_priority");
		$objData->setType("CCM_LISTBOX");
		$objData->setLabel("Customer Priority");
		$attrData->addDataObject($objData);

		my $objData = new ChangeSynergy::apiObjectData();
		$objData->setName("version_fixed");
		$objData->setType("CCM_STRING");
		$objData->setLabel("Version Fixed");
		$attrData->addDataObject($objData);

		$tmp = $csapi->SetAttributes($aUser, "dwarves", $tmp);

		print $tmp->getResponseData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<setUpConnection>

Set up the connection information for calling api functions.

 Parameters:
	scalar protocol: The Web/WWW/Internet protocol
	scalar host    : The fully qualified host name. (Internet)
	                 The machine name. (Intranet)
	scalar port    : The port number for the web site.

 Example:

	my $csapi = new ChangeSynergy::csapi();

 	eval
	{
 		$csapi->setUpConnection("http", "angler", 8600); // Intranet
		or
 		$csapi->setUpConnection("http", "angler.telelogic.com", 80); // Internet
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<setReportConfigType>

Set up the config type to use when running a report.  There are four config
types that can be specified, user, shared, system and all.  The user config type
will only search the users saved information.  The shared config type will only search
the shared config and system will only search the system config.  All will
search the user, then shared and finally the system config and run the the first
report that matches the request.

 Parameters:
	scalar configType: The config entry to search through for the report.
	
	Valid Config Types: These are defined in the Globals class.
        $self->{ALL}       		// User, Shared and System. Returns the first one found.
        $self->{USER_PROFILE}	// A single users profile data.
        $self->{SHARED_PROFILE} // The shared profile data.
	    $self->{SYSTEM_CONFIG}  // The system config data.

 Example:

	my $csapi = new ChangeSynergy::csapi();

 	eval
	{
		my $globals = new ChangeSynergy::Globals();
		
		$csapi->setUpConnection("http", "angler", 8600);
		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");
		
		
		#set the config type for the report.
 		$csapi->setReportConfigType($globals->{USER_PROFILE});
 		or
 		$csapi->setReportConfigType($globals->{SHARED_PROFILE});
 		or
 		$csapi->setReportConfigType($globals->{SYSTEM_CONFIG});
 		or
 		$csapi->setReportConfigType($globals->{ALL});
	
		my $tmpstr = $csapi->ImmediateReportHtml($aUser, "Basic Summary", "Basic Summary Report");
 		
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<setQueryConfigType>

Set up the config type to use when running a query.  There are four config
types that can be specified, user, shared, system and all.  The user config type
will only search the users saved information.  The shared config type will only search
the shared config and system will only search the system config.  All will
search the user, then shared and finally the system config and run the the first
query that matches the request.

 Parameters:
	scalar configType: The config entry to search through for the query.
	
	Valid Config Types: These are defined in the Globals class.
        $self->{ALL}       		// User, Shared and System. Returns the first one found.
        $self->{USER_PROFILE}	// A single users profile data.
        $self->{SHARED_PROFILE} // The shared profile data.
	    $self->{SYSTEM_CONFIG}  // The system config data.

 Example:

	my $csapi = new ChangeSynergy::csapi();

 	eval
	{
		my $globals = new ChangeSynergy::Globals();
		
				
		#set the config type for the query.
 		$csapi->setQueryConfigType($globals->{USER_PROFILE});
 		or
 		$csapi->setQueryConfigType($globals->{SHARED_PROFILE});
 		or
 		$csapi->setQueryConfigType($globals->{SYSTEM_CONFIG});
 		or
 		$csapi->setQueryConfigType($globals->{ALL});
 		
 		#set the config type for the report format.
 		$csapi->setReportConfigType($globals->{USER_PROFILE});
 		or
 		$csapi->setReportConfigType($globals->{SHARED_PROFILE});
 		or
 		$csapi->setReportConfigType($globals->{SYSTEM_CONFIG});
 		or
 		$csapi->setReportConfigType($globals->{ALL});
	
		my $tmpstr = $csapi->ImmediateReportHtml($aUser, "Basic Summary", "Basic Summary Report");
 		
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ShowCRHtml>

Show the details of a Change Request as an HTML web page. The SYNERGY/Change
server determines which template to use. The return result is an
instance of the L<apiData> class.

 Note: The return value is a complete HTML page. <HTML>...</HTML>
       The return value can be saved as a .html file, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar  relationName : A valid CMSynergy/SYNERGY/Change relation name.
	scalar  isModifiable : A string representation of either: ["true"|"false"].

 Returns: apiData
	the complete show form as an html page.

 Example:
 
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ShowCRHtml($aUser, "1347", "child_cr", "true");
	};

	if ($@)
	{
		print $@;
	}

=cut

#############################################################################

=item B<ShowCRHtml>

Show the details of a Change Request as an HTML web page. The
SYNERGY/Change server uses the template name provided. The return 
result is an instance of the L<apiData> class.

 Note: The return value is a complete HTML page. <HTML>...</HTML>
       The return value can be saved as a .html file, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar  templateName : The name of the SYNERGY/Change template to load 
	                       ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).
	scalar  relationName : A valid CMSynergy/SYNERGY/Change relation name.
	scalar  isModifiable : A string representation of either: ["true"|"false"].

Returns: apiData
	the complete show form as an html page.

 Example:
 
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ShowCRHtml($aUser, "1347", "CRDetail", undef, undef);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ShowCRUrl>

Show the details of a Change Request as an HTML web page. The SYNERGY/Change
server determines which template to use. The return result is an
instance of the L<apiData> class.

 Note: The return value is a complete URL address
       The return value can be saved as a link, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar  relationName : A valid CMSynergy/SYNERGY/Change relation name.
	scalar  isModifiable : A string representation of either: ["true"|"false"].

 Returns: apiData
	the complete show form as an html page.

 Example:
 
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ShowCRUrl($aUser, "1347", "child_cr", "true");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ShowCRUrl>

Show the details of a Change Request as an HTML web page. The
SYNERGY/Change server uses the template name provided. The return 
result is an instance of the L<apiData> class.

 Note: The return value is a complete URL address.
       The return value can be saved as a link, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar  templateName : The name of the SYNERGY/Change template to load 
	                       ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).
	scalar  relationName : A valid CMSynergy/SYNERGY/Change relation name.
	scalar  isModifiable : A string representation of either: ["true"|"false"].

Returns: apiData
	the show form as a URL address.

 Example:
 
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ShowCRUrl($aUser, "1347", "CRDetail", undef, undef);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ShowTaskHtml>

Show the details of a Task as an HTML web page. The SYNERGY/Change server
determines which template to use, based on the Task's current status value.
The return result is an instance of the L<apiData> class.

 Note: The return value is a complete HTML page. <HTML>...</HTML>
       The return value can be saved as a .html file, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  taskNumber  : The Task ID to reference.
	scalar  relationName: A valid CMSynergy/SYNERGY/Change relation name.
	scalar  isModifiable: A string representation of either: ["true"|"false"].

 Returns: apiData
	the show task details page as an HTML page.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ShowTaskHtml($aUser, "1", undef, undef);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ShowTaskHtml>

Show the details of a Task as an HTML web page. The SYNERGY/Change server
uses the provided template name. The return result is an instance
of the L<apiData> class.

 Note: The return value is a complete HTML page. <HTML>...</HTML>
       The return value can be saved as a .html file, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  taskNumber  : The Task ID to reference.
	scalar  templateName: The name of the SYNERGY/Change template to load 
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).
	scalar  relationName: A valid CMSynergy/SYNERGY/Change relation name.
	scalar  isModifiable: A string representation of either: ["true"|"false"].

 Returns: apiData
	the show task details page as an HTML page.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ShowTaskHtml($aUser, "1", "TaskDetails", undef, undef);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ShowTaskUrl>

Show the details of a Task as an HTML web page. The SYNERGY/Change server
determines which template to use, based on the Task's current status value.
The return result is an instance of the L<apiData> class.

 Note: The return value is a complete URL address.
       The return value can be saved as a link, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  taskNumber  : The Task ID to reference.
	scalar  relationName: A valid CMSynergy/SYNERGY/Change relation name.
	scalar  isModifiable: A string representation of either: ["true"|"false"].

 Returns: apiData
	the URL to the show task details page.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ShowTaskUrl($aUser, "1", undef, undef);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ShowTaskUrl>

Show the details of a Task as an HTML web page. The SYNERGY/Change server
uses the provided template name. The return result is an instance 
of the L<apiData> class.

 Note: The return value is a complete URL address.
       The return value can be saved as a link, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  taskNumber  : The Task ID to reference.
	scalar  templateName: The name of the SYNERGY/Change template to load 
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).
	scalar  relationName: A valid CMSynergy/SYNERGY/Change relation name.
	scalar  isModifiable: A string representation of either: ["true"|"false"].

 Returns: apiData
	the URL to the show task details page.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ShowTaskUrl($aUser, "1", "TaskDetails", undef, undef);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<StartServerAccess>

Restart server access on the SYNERGY/Change Server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->StartServerAccess($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<StopServerAccess>

Stop server access on the SYNERGY/Change Server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->StopServerAccess($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<SubmitCR>

Apply the modified Change Request data. Only data objects that have 
been flagged as modified are submitted to the SYNERGY/Change server. 
The attributes problem_number, modify_time, and cvid should 
not be altered. The api classes will automatically process these attributes
when needed. The return result is an instance of the L<apiData> class.

Note: The L<apiObjectData>'s member method setValue("") will automatically set
the modified flag when invoked.

 Parameters:
	apiUser         aUser: The current api user's login data.
	apiObjectVector data : The data to be processed by the api function.
 
 Returns: apiData
	results on if the submit was successful	
 
 Example:

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->SubmitCRData($aUser, "START_HERE2entered");

		my $i;
		my $j = $tmp->getDataSize();

		for($i=0;$i<$j;$i++)
		{
			if($tmp->getDataObject($i)->getRequired())
			{
				$tmp->getDataObject($i)->setValue("I must supply a value here to successfully complete a submit...");
			}
		}

		$tmp->getDataObjectByName("problem_synopsis")->setValue("I submitted this through the csapi");
		$tmp->getDataObjectByName("problem_description")->setValue("Yes, isn't this great!!!!");
		$tmp->getDataObjectByName("severity")->setValue("Showstopper");
		$tmp->getDataObjectByName("product_name")->setValue("Product A");
		$tmp->getDataObjectByName("submitter")->setValue("u00001");
		$tmp->getDataObjectByName("request_type")->setValue("Defect");

		$tmp->getDataObjectByName("crstatus")->setValue($tmp->getTransitionLink(0)->getToState());
		
		my $tmpstr = $csapi->SubmitCR($aUser, $tmp);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<SubmitCRAssocCR>

Apply the modified Change Request data. Only data objects that have been
flagged as modified are submitted to the SYNERGY/Change server. The attributes
problem_number, modify_time, and cvid should not be altered. The api classes
will automatically process these attributes when needed. The return result is
an instance of the L<apiData> class.

Note: The L<apiObjectData>'s member method setValue("") will automatically set
the modified flag when invoked.

 Parameters:
	apiUser         aUser        : The current api user's login data.
	apiObjectVector data         : The data to be processed by the api function.
	scalar          relationName : A valid CMSynergy/SYNERGY/Change relation name.
	scalar          problemNumber: The Change Request ID/Problem Number ID to reference.
 
 Returns: apiData
	results on if the submit and association was successful	
 
 Example 1:
 
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->SubmitCRData($aUser, "START_HERE2entered");

		my $i;
		my $j = $tmp->getDataSize();

		for($i=0;$i<$j;$i++)
		{
			if($tmp->getDataObject($i)->getRequired())
			{
				$tmp->getDataObject($i)->setValue("I must supply a value here to successfully complete a submit...");
			}
		}

		$tmp->getDataObjectByName("problem_synopsis")->setValue("I submitted this through the csapi");
		$tmp->getDataObjectByName("problem_description")->setValue("Yes, isn't this great!!!!");
		$tmp->getDataObjectByName("severity")->setValue("Showstopper");
		$tmp->getDataObjectByName("product_name")->setValue("Product A");
		$tmp->getDataObjectByName("submitter")->setValue($aUser->getUserName());
		$tmp->getDataObjectByName("request_type")->setValue("Defect");

		$tmp->getDatagetDataObjectByNameObject("crstatus")->setValue($tmp->getTransitionLink(0)->getToState());
		
		$tmpstr = $csapi->SubmitCRAssocCR($aUser, $tmp, "child_cr", "1347");
	};

	if ($@)
	{
		print $@;
	}

 Example 2:
 
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->CopyCRData($aUser, "1347", "COPY_child_cr2new_child");

		my $i;
		my $j = $tmp->getDataSize();

		for($i=0;$i<$j;$i++)
		{
			if($tmp->getDataObject($i)->getRequired())
			{
				$tmp->getDataObject($i)->setValue("I must supply a value here to successfully complete a submit...");
			}

			if($tmp->getDataObject($i)->getInherited())
			{
				$tmp->getDataObject($i)->setIsModified(TRUE);
			}
		}

		$tmp->getDataObjectByName("problem_synopsis")->setValue("I submitted this through the csapi");
		$tmp->getDataObjectByName("problem_description")->setValue("Yes, isn't this great!!!!");
		$tmp->getDataObjectByName("severity")->setValue("Showstopper");
		$tmp->getDataObjectByName("product_name")->setValue("Product A");
		$tmp->getDataObjectByName("submitter")->setValue("u00001");
		$tmp->getDataObjectByName("request_type")->setValue("Defect");

		$tmp->getDataObject("crstatus")->setValue($tmp->getTransitionLink(0)->getToState());
		
		my $tmpstr = $csapi->SubmitCRAssocCR($aUser, $tmp, $tmp->getTransitionLink(0)->getRelation(), "1347");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<SubmitCRData>

Load the requirements of a Change Request submission into data classes
in which the details of the new Change Request can be modified. The modified
data classes can then be submitted using one of the modification api 
functions to change a Change Request. The return result is an instance
of the L<apiObjectVector> class.
 
Note: The submit "to state" is provided with this api function call.
See L<apiTransitions> class description.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  templateName: The name of the SYNERGY/Change template to load
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).

 Returns: apiObjectVector
	the requirements of a CR submission in data format
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->SubmitCRData($aUser, "START_HERE2entered");

		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<SubmitCRHtml>

Load, as an HTML web page, the requirements to submit a Change Request.
The return result is an instance of the L<apiData> class.

 Note: The return value is a complete HTML page. <HTML>...</HTML>
       The return value can be saved as a .html file, or loaded
       into a browser window/control.
	   
 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  templateName : The name of the SYNERGY/Change template to load
	                       ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar  relationName : A valid CMSynergy/SYNERGY/Change relation name.
	scalar  externalData : A string of XML data to pass to a submit request.
 
 Format of External Data XML:
 
 <EXTERNAL_CONTEXT_DATA>
 	<ATTRIBUTE NAME="attribute_name">your value</ATTRIBUTE>
 	<ATTRIBUTE NAME="attribute_name">your value</ATTRIBUTE>
 	<ATTRIBUTE NAME="attribute_name">your value</ATTRIBUTE>
 	.
 	.
 	.
 </EXTERNAL_CONTEXT_DATA>
 
 Returns: apiData
	the submit CR page requested as an html page.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->SubmitCRHtml($aUser, "CRSubmit", undef, undef, undef);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<SubmitCRUrl>

Load, as an HTML web page, the requirements to submit a Change Request.
The return result is an instance of the L<apiData> class.

 Note: The return value is a complete URL address.
       The return value can be saved as a link, or loaded
       into a browser window/control.
	   
 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  templateName : The name of the SYNERGY/Change template to load ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).
	                       ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar  relationName : A valid CMSynergy/SYNERGY/Change relation name.
	scalar  externalData : A string of XML data to pass to a submit request.
 
 Format of External Data XML:
 
 <EXTERNAL_CONTEXT_DATA>
 	<ATTRIBUTE NAME="attribute_name">your value</ATTRIBUTE>
 	<ATTRIBUTE NAME="attribute_name">your value</ATTRIBUTE>
 	<ATTRIBUTE NAME="attribute_name">your value</ATTRIBUTE>
 	.
 	.
 	.
 </EXTERNAL_CONTEXT_DATA>
 
 Returns: apiData
	the submit CR page requested as an html page.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->SubmitCRUrl($aUser, "CRSubmit", undef, undef, undef);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<SubmitTask>

Apply the modified Task data. Only data objects that have been flagged as
modified are submitted to the SYNERGY/Change server. The attributes task_number,
modify_time, and cvid should not be altered. The api classes will automatically
process these attributes when needed. The return result is an instance of 
the L<apiData> class.

Note: The L<apiObjectData>'s member method setValue("") will automatically set
the modified flag when invoked.

 Parameters:
	apiUser         aUser: The current api user's login data.
	apiObjectVector data : The data to be processed by the api function.

 Returns: apiData
	results on if the submit was successful	

 Example 1:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->SubmitTaskData($aUser, "TaskCreate");
		
		my $i;
		my $j = $tmp->getDataSize();

		for($i=0;$i<$j;$i++)
		{
			if($tmp->getDataObject($i)->getRequired())
			{
				$tmp->getDataObject($i)->setValue("I must supply a value here to successfully complete a submit...");
			}
		}

		$tmp->getDataObjectByName("task_synopsis")->setValue("I modified the synopsis through the csapi...");
		$tmp->getDataObjectByName("task_description")->setValue("I modified the description through the csapi...");
		$tmp->getDataObjectByName("priority")->setValue("high");
		$tmp->getDataObjectByName("resolver")->setValue($aUser->getUserName());

		my $tmpstr = $csapi->SubmitTask($aUser, $tmp);
	};


	if ($@)
	{
		print $@;
	}


 Example 2:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->CopyTaskData($aUser, "12", "CreateTask");
		
		my $i;
		my $j = $tmp->getDataSize();

		for($i=0;$i<$j;$i++)
		{
			if($tmp->getDataObject($i)->getRequired())
			{
				if($tmp->getDataObject($i)->getValue() == NULL)
					$tmp->getDataObject($i)->setValue("I must supply a value here to successfully complete a submit...");
			}
		}

		$tmp->getDataObjectByName("task_synopsis")->setValue("I modified the synopsis through the csapi...");
		$tmp->getDataObjectByName("task_description")->setValue("I modified the description through the csapi...");
		$tmp->getDataObjectByName("priority")->setValue("high");
		$tmp->getDataObjectByName("resolver")->setValue($aUser->getUserName());

		my $tmpstr = $csapi->SubmitTask($aUser, $tmp);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<SubmitTaskAssocCR>

Apply the modified Task data. Only data objects that have been flagged as
modified are submitted to the SYNERGY/Change server. The attributes task_number, 
modify_time, and cvid should not be altered. The api classes will automatically
process these attributes when needed. The return result is an instance of the 
L<apiData> class.

Note: The L<apiObjectData>'s member method setValue("") will automatically set
the modified flag when invoked.

 Parameters:
	apiUser         aUser        : The current api user's login data.
	apiObjectVector data         : The data to be processed by the api function.
	scalar          relationName : A valid CMSynergy/SYNERGY/Change relation name.
	scalar          problemNumber: The Change Request ID/Problem Number ID to reference.

 Returns: apiData
	results on if the submit and association was successful	

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->SubmitTaskData($aUser, "TaskCreate");
		
		my $i;
		my $j = $tmp->getDataSize();

		for($i=0;$i<$j;$i++)
		{
			if($tmp->getDataObject($i)->getRequired())
			{
				$tmp->getDataObject($i)->setValue("I must supply a value here to successfully complete a submit...");
			}
		}

		$tmp->getDataObjectByName("task_synopsis")->setValue("I modified the synopsis through the csapi...");
		$tmp->getDataObjectByName("task_description")->setValue("I modified the description through the csapi...");
		$tmp->getDataObjectByName("priority")->setValue("high");
		$tmp->getDataObjectByName("resolver")->setValue($aUser->getUserName());

		my $tmpstr = $csapi->SubmitTaskAssocCR($aUser, $tmp, "associated_task", "1355");
	};


	if ($@)
	{
		print $@;
	}

=cut

##############################################################################


=item B<SubmitTaskData>

Load the requirements of a Task submission into data classes in which 
the details of the new Task can be modified. The modified data classes
can then be submitted using one of the modification api functions 
to change a Task. The return result is an instance of the L<apiObjectVector> class.

 Parameters:
 	apiUser aUser       : The current api user's login data.
	scalar  templateName: The name of the SYNERGY/Change template to load
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).

 Returns: apiObjectVector
	the requirements of a task submission in data format.

 Example:
 
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->SubmitTaskData($aUser, "CreateTask");

		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<SubmitTaskHtml>

Load, as an HTML web page, the requirements to submit a Task.
The return result is an instance of the L<apiData> class.

 Note: The return value is a complete HTML page. <HTML>...</HTML>
       The return value can be saved as a .html file, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  templateName: The name of the SYNERGY/Change template to load 
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).

 Returns: apiData
	the submit task page requested as an html page.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->SubmitTaskHtml($aUser, "TaskCreate");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<SubmitTaskUrl>

Load, as an HTML web page, the requirements to submit a Task.
The return result is an instance of the L<apiData> class.

 Note: The return value is a complete URL address.
       The return value can be saved as a link, or loaded
       into a browser window/control.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  templateName: The name of the SYNERGY/Change template to load 
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).

 Returns: apiData
	the URL for the submit Task page.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->SubmitTaskUrl($aUser, "TaskCreate");
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<TaskFullName>

Construct a four part name for a task. The actual existance of the task is not
checked; this only constructs the four part name.
 
 Parameters:

	apiUser aUser         : The current api user's login data.
	scalar  taskNumber: The task number.
 
 Returns: scalar
	The four part name.

=cut

##############################################################################

=item B<ToggleDebug>

Toggle the debug flag on the SYNERGY/Change server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->ToggleDebug($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<TransitionCR>

Apply the modified Change Request data. Only data objects that have been
flagged as modified are submitted to the SYNERGY/Change server. The attributes
problem_number, modify_time, and cvid should not be altered. The api classes 
will automatically process these attributes when needed. The return result is
an instance of the L<apiData> class.
 
Note: The apiObjectData's member method setValue("") will automatically set
the modified flag when invoked.

 Parameters:
	apiUser         aUser: The current api user's login data.
	apiObjectVector data : The data to be processed by the api function.

 Returns: apiData
	results on if the transition was successful
 
 Example:
 
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp1 = $csapi->AttributeModifyCRData($aUser, "100", "crstatus");
		or
		my $tmp1 = $csapi->AttributeModifyCRData($aUser, "100");
		or
		my $tmp1 = $csapi->ModifyCRData($aUser, "100", "CRDetail");
		or
		my $tmp1 = $csapi->GetCRData($aUser, "100", "problem_synopsis|problem_description|keyword");
		
		my $tmp2 = $csapi->TransitionCRData($aUser, "100", $tmp1->getTransitionLink(1)->getTransition());

		$tmp2->getDataObjectByName("problem_synopsis")->setValue("I modified the synopsis through the csapi...");
		$tmp2->getDataObjectByName("problem_description")->setValue("I modified the description through the csapi...");
		$tmp2->getDataObjectByName("keyword")->setValue("csapi");

  		$tmp2->getDataObjectByName("crstatus")->setValue($tmp1->getTransitionLink(1)->getToState());

		my $tmpstr = $csapi->TransitionCR($aUser, $tmp2);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<TransitionCRData>

Load the details of a Change Request into data classes in which the 
details of the Change Request can be modified. The modified data classes
can then be submitted using one of the modification api functions 
to change a Change Request. The return result is an instance of the
L<apiObjectVector> class.

Note: The transition's "from state" and "to state" are provided with this api function call.
See L<apiTransitions> class description.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The Change Request ID/Problem Number ID to reference.
	scalar  templateName : The name of the SYNERGY/Change template to load
	                       ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).

 Returns: apiObjectVector
	the details of a change request in data format.

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->TransitionCRData($aUser, "100", ""assigned2resolved");

		my $tmpstr = tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<TransitionTask>

Apply the modified Task data. Only data objects that have been flagged
as modified are submitted to the SYNERGY/Change server. The attributes 
task_number, modify_time, and cvid should not be altered. The api classes
will automatically process these attributes when needed.

Note: The L<apiObjectData>'s member method setValue("") will automatically set
the modified flag when invoked.

 Parameters:
	apiUser         aUser: The current api user's login data.
	apiObjectVector data : The data to be processed by the api function.

 Returns: apiData
	results on if the transition was successful

 Example:
 
	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->AttributeModifyTaskData($aUser, "10", "status");
		or
		my $tmp = $csapi->AttributeModifyTaskData($aUser, "10");
		or
		my $tmp = $csapi->ModifyTaskData($aUser, "10", "TaskDetails");
		or
		my $tmp = $csapi->GetTaskData($aUser, "10", "task_synopsis|task_description|priority");
		or
		my $tmp = $csapi->TransitionTaskData($aUser, "10", "TaskDetails");
		
		$tmp->getDataObjectByName("task_synopsis")->setValue("I modified the synopsis through the csapi...");
		$tmp->getDataObjectByName("task_description")->setValue("I modified the description through the csapi...");
		$tmp->getDataObjectByName("priority")->setValue("high");

		$tmp->getDataObjectByName("status")->setValue("completed");

		my $tmpstr = $csapi->TransitionTask($aUser, $tmp);
	};


	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<TransitionTaskData>

Load the details of a Task into data classes in which the details
of the Task can be modified. The modified data classes can then 
be submitted using one of the modification api functions to change a Task.
The return result is an instance of the L<apiObjectVector> class.

 Parameters:
	apiUser aUser       : The current api user's login data.
	scalar  taskNumber  : The Task ID to reference.
	scalar  templateName: The name of the SYNERGY/Change template to load
	                      ([CCM_TEMPLATE][NAME]template name[/NAME]...[/CCM_TEMPLATE]).

 Returns: apiObjectVector
	the details of a task in data format.	

 Example:
 
	my $csapi = new ChangeSynergy::csapi();
	
	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->TransitionTaskData($aUser, "4", "TaskDetails");

		my $tmpstr = $tmp->getXmlData();
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<UpdateIndex>

Update the search index on the SYNERGY/Change Server.
The return result is an instance of the L<apiData> class.

 Parameters:
	apiUser aUser: The current api user's login data.

 Returns: apiData
	the return message from the server.
 
 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmpstr = $csapi->UpdateIndex($aUser);
	};

	if ($@)
	{
		print $@;
	}

=cut

##############################################################################

=item B<ValidateLicense>

Validate if this license can be obtained.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  licenseString: The license identifier to be validated.
 
 Returns: scalar
	true or false

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "Admin", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->ValidateLicense($aUser, "pt");
	};

	if ($@)
	{
		print $@;
	}

=cut

###############################################################################

=item B<VerifySignatures>

Verifies a Change Request's electronic signatures on a specified CCM_E_SIGNATURE
attribute.

 Parameters:
	apiUser aUser        : The current api user's login data.
	scalar  problemNumber: The problem number to verify.
	scalar  attributeName: The eleectronic signature attribute name.
 
 Returns: scalar
	true or false

 Example:

	my $csapi = new ChangeSynergy::csapi();

	eval
	{
		$csapi->setUpConnection("http", "angler", 8600);

		my $aUser = $csapi->Login("u00001", "u00001", "User", "\\\\angler\\ccmdb\\cm_database");

		my $tmp = $csapi->VerifySignatures($aUser, "1", "myEig");
	};

	if ($@)
	{
		print $@;
	}

=cut

###############################################################################
